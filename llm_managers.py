from abc import ABC, abstractmethod

import torch
import transformers
from transformers import AutoTokenizer, BitsAndBytesConfig
from transformers.generation import GenerationConfig
from huggingface_hub import login

import os


class LlmManager(ABC):
    """
    An "interface" for various LLM manager objects.
    """

    @abstractmethod
    def chat_completion(
        self,
        prompt,
        print_result=False,
        seed=42,
        max_new_tokens=128,
        do_sample=True,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.0,
    ):
        pass


class HuggingFaceLlmManager(LlmManager):
    def __init__(
        self,
        model_name,
        cache_dir="/vol/bitbucket/jl8420/legal_nlp_asp_cache",
        model_args=None,
        input_device="cuda:0",
        quantization="4bit",
    ):
        super().__init__()
        if quantization == "4bit":
            quantization_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.bfloat16,
            )
        elif quantization == "8bit":
            quantization_config = BitsAndBytesConfig(
                load_in_8bit=True,
            )
        elif quantization == "none":
            quantization_config = None
        else:
            raise ValueError(f"Invalid quantization value {quantization}")
        
        login(token='')

        self.tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=model_name,
            device_map="auto",
            model_kwargs={
                "torch_dtype": torch.float16 if "gemma" not in model_name else torch.bfloat16,
                "quantization_config": quantization_config,
                "cache_dir": cache_dir,
            },
        )
        self.input_device = input_device

    def chat_completion(
        self,
        message,
        print_result=False,
        seed=42,
        max_new_tokens=128,
        do_sample=True,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.0,
        trim_response=True,
        apply_template=True,
    ):
        transformers.set_seed(seed)
        messages = [{"role": "user", "content": message}]
        if apply_template:
            prompt = self.pipeline.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        else:
            prompt = message
        
        response = self.pipeline(
            prompt,
            max_new_tokens=max_new_tokens,
            do_sample=do_sample,
            temperature=temperature,
            top_p=top_p,
            repetition_penalty=repetition_penalty,
            prefix_allowed_tokens_fn=prefix_allowed_tokens_fn,
        )[0]["generated_text"]

        if print_result:
            print(response, flush=True)

        if trim_response:
            response = response.replace(prompt, "").strip()

        return response

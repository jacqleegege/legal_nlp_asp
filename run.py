import llm_managers as llm

llm_manager = llm.HuggingFaceLlmManager( model_name= "meta-llama/Llama-2-13b-hf")

prompt = """You are a system responsible with translating natural language legal cases to its ASP form
You need to follow the format of the given examples. Here are some examples to learn from:
% Text
% Alice is married under section 7703 for the year 2017. Alice files a joint return with her spouse for 2017. Alice's and her spouse's taxable income for the year 2017 is $42876.

% Question
% Alice and her spouse have to pay $7208 in taxes for the year 2017 under section 1(a)(i). Contradiction

% Facts
person(alice_s1_a_1_i_neg).
person(spouse_s1_a_1_i_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(42876).
finance(7208).
s7703(alice_s1_a_1_i_neg,spouse_s1_a_1_i_neg,alice_and_spouse_s1_a_1_i_neg,2017).
marriage_(alice_and_spouse_s1_a_1_i_neg).
joint_return_(joint_return_s1_a_1_i_neg).
agent_(joint_return_s1_a_1_i_neg,alice_s1_a_1_i_neg).
agent_(joint_return_s1_a_1_i_neg,spouse_s1_a_1_i_neg).
start_(joint_return_s1_a_1_i_neg,d2017_01_01).
end_(joint_return_s1_a_1_i_neg,d2017_12_31).
s63(alice_s1_a_1_i_neg,2017,42876).

% Test
:- \+ s1_a_i(42876,7208).
:- halt.

Above is the first example.Below are more examples:
% Text
% Alice is married under section 7703 for the year 2017. Alice files a joint return with her spouse for 2017. Alice's and her spouse's taxable income for the year 2017 is $17330.

% Question
% Alice and her spouse have to pay $2600 in taxes for the year 2017 under section 1(a)(i). Entailment

% Facts
person(alice_s1_a_1_i_pos).
person(spouse_s1_a_1_i_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(17330).
finance(2600).
s7703(alice_s1_a_1_i_pos,spouse_s1_a_1_i_pos,alice_and_spouse_s1_a_1_i_pos,2017).
marriage_(alice_and_spouse_s1_a_1_i_pos).
marriage_(alice_and_spouse_s1_a_1_i_pos).
joint_return_(joint_return_s1_a_1_i_pos).
agent_(joint_return_s1_a_1_i_pos,alice_s1_a_1_i_pos).
agent_(joint_return_s1_a_1_i_pos,spouse_s1_a_1_i_pos).
start_(joint_return_s1_a_1_i_pos,d2017_01_01).
end_(joint_return_s1_a_1_i_pos,d2017_12_31).
s63(alice_s1_a_1_i_pos,2017,17330).

% Test
:- s1_a_i(17330,2600).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice files a joint return with her spouse for 2017. Alice's and her spouse_s1_a_ii_neg's taxable income for the year 2017 is $103272.

% Question
% Alice and her spouse have to pay $24543 in taxes for the year 2017 under section 1(a)(ii). Contradiction

% Facts
person(alice_s1_a_1_ii_neg).
person(spouse_s1_a_1_ii_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(103272).
finance(24543).

s7703(alice_s1_a_1_ii_neg,spouse_s1_a_1_ii_neg,alice_and_spouse_s1_a_1_ii_neg,2017).
marriage_(alice_and_spouse_s1_a_1_ii_neg).
joint_return_(joint_return_s1_a_1_ii_neg).
agent_(joint_return_s1_a_1_ii_neg,alice_s1_a_1_ii_neg).
agent_(joint_return_s1_a_1_ii_neg,spouse_s1_a_1_ii_neg).
start_(joint_return_s1_a_1_ii_neg,d2017_01_01).
end_(joint_return_s1_a_1_ii_neg,d2017_12_31).
s63(alice_s1_a_1_ii_neg,2017,103272).

% Test
:- \+ s1_a_ii(103272,24543).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice files a joint return with her spouse for 2017. Alice's and her spouse's taxable income for the year 2017 is $42876.

% Question
% Alice and her spouse have to pay $7208 in taxes for the year 2017 under section 1(a)(ii). Entailment

% Facts
person(alice_s1_a_1_ii_pos).
person(spouse_s1_a_1_ii_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(42876).
finance(7208).

s7703(alice_s1_a_1_ii_pos,spouse_s1_a_1_ii_pos,alice_and_spouse_s1_a_1_ii_pos,2017).
marriage_(alice_and_spouse_s1_a_1_ii_pos).
joint_return_(joint_return_s1_a_1_ii_pos).
agent_(joint_return_s1_a_1_ii_pos,alice_s1_a_1_ii_pos).
agent_(joint_return_s1_a_1_ii_pos,spouse_s1_a_1_ii_pos).
start_(joint_return_s1_a_1_ii_pos,d2017_01_01).
end_(joint_return_s1_a_1_ii_pos,d2017_12_31).
s63(alice_s1_a_1_ii_pos,2017,42876).

% Test
:- s1_a_ii(42876,7208).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice files a joint return with her spouse for 2017. Alice's and her spouse's taxable income for the year 2017 is $164612.

% Question
% Alice and her spouse have to pay $44789 in taxes for the year 2017 under section 1(a)(iii). Contradiction

% Facts
person(alice_s1_a_1_iii_neg).
person(spouse_s1_a_1_iii_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(164612).
finance(44789).

s7703(alice_s1_a_1_iii_neg,spouse_s1_a_1_iii_neg,alice_and_spouse_s1_a_1_iii_neg,2017).
marriage_(alice_and_spouse_s1_a_1_iii_neg).
joint_return_(joint_return_s1_a_1_iii_neg).
agent_(joint_return_s1_a_1_iii_neg,alice_s1_a_1_iii_neg).
agent_(joint_return_s1_a_1_iii_neg,spouse_s1_a_1_iii_neg).
start_(joint_return_s1_a_1_iii_neg,d2017_01_01).
end_(joint_return_s1_a_1_iii_neg,d2017_12_31).
s63(alice_s1_a_1_iii_neg,2017,164612).

% Test
:- \+ s1_a_iii(164612,44789).
:- halt.
% Text
% alice_s1_a_iii_pos is married under section 7703 for the year 2017. alice_s1_a_iii_pos files a joint return with her spouse_s1_a_iii_pos for 2017. alice_s1_a_iii_pos's and her spouse_s1_a_iii_pos's taxable income for the year 2017 is $103272.

% Question
% alice_s1_a_iii_pos and her spouse_s1_a_iii_pos have to pay $24543 in taxes for the year 2017 under section 1(a)(iii). Entailment

% Facts
person(alice_s1_a_1_iii_pos).
person(spouse_s1_a_1_iii_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(103272).
finance(24543).

s7703(alice_s1_a_1_iii_pos,spouse_s1_a_1_iii_pos,alice_and_spouse_s1_a_1_iii_pos,2017).
s7703_short(alice_s1_a_1_iii_pos,spouse_s1_a_1_iii_pos,2017).
marriage_(alice_and_spouse_s1_a_1_iii_pos).
joint_return_(joint_return_s1_a_1_iii_pos).
agent_(joint_return_s1_a_1_iii_pos,alice_s1_a_1_iii_pos).
agent_(joint_return_s1_a_1_iii_pos,spouse_s1_a_1_iii_pos).
start_(joint_return_s1_a_1_iii_pos,d2017_01_01).
end_(joint_return_s1_a_1_iii_pos,d2017_12_31).
s63(alice_s1_a_1_iii_pos,2017,103272).

% Test
:- s1_a_iii(103272,24543).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice files a joint return with her spouse for 2017. Alice's and her spouse's taxable income for the year 2017 is $684642.

% Question
% Alice and her spouse have to pay $247647 in taxes for the year 2017 under section 1(a)(iv). Contradiction

% Facts
person(alice_s1_a_1_iv_neg).
person(spouse_s1_a_1_iv_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(684642).
finance(247647).

s7703(alice_s1_a_1_iv_neg,spouse_s1_a_1_iv_neg,alice_and_spouse_s1_a_1_iv_neg,2017).
marriage_(alice_and_spouse_s1_a_1_iv_neg).
joint_return_(joint_return_s1_a_1_iv_neg).
agent_(joint_return_s1_a_1_iv_neg,alice_s1_a_1_iv_neg).
agent_(joint_return_s1_a_1_iv_neg,spouse_s1_a_1_iv_neg).
start_(joint_return_s1_a_1_iv_neg,d2017_01_01).
end_(joint_return_s1_a_1_iv_neg,d2017_12_31).
s63(alice_s1_a_1_iv_neg,2017,684642).

% Test
:- \+ s1_a_iv(684642,247647).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice files a joint return with her spouse for 2017. Alice's and her spouse's taxable income for the year 2017 is $164612.

% Question
% Alice and her spouse have to pay $44789 in taxes for the year 2017 under section 1(a)(iv). Entailment

% Facts
person(alice_s1_a_1_iv_pos).
person(spouse_s1_a_1_iv_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(164612).
finance(44789).

s7703(alice_s1_a_1_iv_pos,spouse_s1_a_1_iv_pos,alice_and_spouse_s1_a_1_iv_pos,2017).
marriage_(alice_and_spouse_s1_a_1_iv_pos).
joint_return_(joint_return_s1_a_1_iv_pos).
agent_(joint_return_s1_a_1_iv_pos,alice_s1_a_1_iv_pos).
agent_(joint_return_s1_a_1_iv_pos,spouse_s1_a_1_iv_pos).
start_(joint_return_s1_a_1_iv_pos,d2017_01_01).
end_(joint_return_s1_a_1_iv_pos,d2017_12_31).
s63(alice_s1_a_1_iv_pos,2017,164612).

% Test
:- s1_a_iv(164612,44789).
:- halt.
% Text
% Alice is a head of household for the year 2017. Alice's taxable income for the year 2017 is $97407.

% Question
% Alice has to pay $24056 in taxes for the year 2017 under section 1(a). Contradiction

% Facts
person(alice_s1_a_1_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(97407).
finance(24056).
% s2_b(alice,_,2017).
s2_b(alice_s1_a_1_neg,alice_s1_a_1_neg,2017).
s63(alice_s1_a_1_neg,2017,97407).

% Test
:- \+ s1_a(alice_s1_a_1_neg,2017,97407,24056).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice files a joint return with her spouse for 2017. Alice's and her husband's taxable income for the year 2017 is $17330.

% Question
% Alice and her husband have to pay $2600 in taxes for the year 2017 under section 1(a). Entailment

% Facts
person(alice_s1_a_1_pos).
person(spouse_s1_a_1_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(17330).
finance(2600).
s7703(alice_s1_a_1_pos,spouse_s1_a_1_pos,alice_and_spouse_s1_a_1_pos,2017).
marriage_(alice_and_spouse_s1_a_1_pos).
joint_return_(joint_return_s1_a_1_pos).
agent_(joint_return_s1_a_1_pos,alice_s1_a_1_pos).
agent_(joint_return_s1_a_1_pos,spouse_s1_a_1_pos).
start_(joint_return_s1_a_1_pos,d2017_01_01).
end_(joint_return_s1_a_1_pos,d2017_12_31).
s63(alice_s1_a_1_pos,2017,17330).

% Test
:- s1_a(alice_s1_a_1_pos,2017,17330,2600).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice files a joint return with her spouse for 2017. Alice's and her spouse's taxable income for the year 2017 is $17330.

% Question
% Alice and her spouse have to pay $2600 in taxes for the year 2017 under section 1(a)(v). Contradiction

% Facts
person(alice_s1_a_1_v_neg).
person(spouse_s1_a_1_v_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(17330).
finance(2600).

s7703(alice_s1_a_1_v_neg,spouse_s1_a_1_v_neg,alice_and_spouse_s1_a_1_v_neg,2017).
marriage_(alice_and_spouse_s1_a_1_v_neg).
joint_return_(joint_return_s1_a_1_v_neg).
agent_(joint_return_s1_a_1_v_neg,alice_s1_a_1_v_neg).
agent_(joint_return_s1_a_1_v_neg,spouse_s1_a_1_v_neg).
start_(joint_return_s1_a_1_v_neg,d2017_01_01).
end_(joint_return_s1_a_1_v_neg,d2017_12_31).
s63(alice_s1_a_1_v_neg,2017,17330).

% Test
:- \+ s1_a_v(17330,2600).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice files a joint return with her spouse for 2017. Alice's and her spouse's taxable income for the year 2017 is $684642.

% Question
% Alice and her spouse have to pay $247647 in taxes for the year 2017 under section 1(a)(v). Entailment

% Facts
person(alice_s1_a_1_v_pos).
person(spouse_s1_a_1_v_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(684642).
finance(247647).

marriage_(alice_and_spouse_s1_a_1_v_pos).
s7703(alice_s1_a_1_v_pos,spouse_s1_a_1_v_pos,alice_and_spouse_s1_a_1_v_pos,2017).
joint_return_(joint_return_s1_a_1_v_pos).
agent_(joint_return_s1_a_1_v_pos,alice_s1_a_1_v_pos).
agent_(joint_return_s1_a_1_v_pos,spouse_s1_a_1_v_pos).
start_(joint_return_s1_a_1_v_pos,d2017_01_01).
end_(joint_return_s1_a_1_v_pos,d2017_12_31).
s63(alice_s1_a_1_v_pos,2017,684642).

% Test
:- s1_a_v(684642,247647).
:- halt.
% Text
% Alice is a surviving spouse for the year 2017. Alice's taxable income for the year 2017 is $70117.

% Question
% Alice has to pay $14836 in taxes for the year 2017 under section 1(a)(i). Contradiction

% Facts
person(alice_s1_a_2_i_neg).
person(spouse_s1_a_2_i_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(70117).
finance(14836).

s2_a(alice_s1_a_2_i_neg,spouse_s1_a_2_i_neg,2017).
s63(alice_s1_a_2_i_neg,2017,70117).

% Test
:- \+ s1_a_i(70117,14836).
:- halt.
% Text
% Alice is a surviving spouse for the year 2017. Alice's taxable income for the year 2017 is $25561.

% Question
% Alice has to pay $3834 in taxes for the year 2017 under section 1(a)(i). Entailment

% Facts
person(alice_s1_a_2_i_pos).
person(spouse_s1_a_2_i_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(25561).
finance(3834).
s2_a(alice_s1_a_2_i_pos,spouse_s1_a_2_i_pos,2017).
s63(alice_s1_a_2_i_pos,2017,25561).

% Test
:- s1_a_i(25561,3834).
:- halt.
% Text
% Alice is a surviving spouse for the year 2017. Alice's taxable income for the year 2017 is $95129.

% Question
% Alice has to pay $22018 in taxes for the year 2017 under section 1(a)(ii). Contradiction

% Facts
person(alice_s1_a_2_ii_neg).
person(spouse_s1_a_2_ii_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(95129).
finance(22018).

s2_a(alice_s1_a_2_ii_neg,spouse_s1_a_2_ii_neg,2017).
s63(alice_s1_a_2_ii_neg,2017,95129).

% Test
:- \+ s1_a_ii(95129,22018).
:- halt.
% Text
% Alice is a surviving spouse for the year 2017. Alice's taxable income for the year 2017 is $70117.

% Question
% Alice has to pay $14836 in taxes for the year 2017 under section 1(a)(ii). Entailment

% Facts
person(alice_s1_a_2_ii_pos).
person(spouse_s1_a_2_ii_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(70117).
finance(14836).

s2_a(alice_s1_a_2_ii_pos,spouse_s1_a_2_ii_pos,2017).
s63(alice_s1_a_2_ii_pos,2017,70117).

% Test
:- s1_a_ii(70117,14836).
:- halt.
% Text
% Alice is a surviving spouse for the year 2017. Alice's taxable income for the year 2017 is $236422.

% Question
% Alice has to pay $70640 in taxes for the year 2017 under section 1(a)(iii). Contradiction

% Facts
person(alice_s1_a_2_iii_neg).
person(spouse_s1_a_2_iii_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(236422).
finance(70640).

s2_a(alice_s1_a_2_iii_neg,spouse_s1_a_2_iii_neg,2017).
s63(alice_s1_a_2_iii_neg,2017,236422).

% Test
:- \+ s1_a_iii(236422,70640).
:- halt.
% Text
% Alice is a surviving spouse for the year 2017. Alice's taxable income for the year 2017 is $95129.

% Question
% Alice has to pay $22018 in taxes for the year 2017 under section 1(a)(iii). Entailment

% Facts
person(alice_s1_a_2_iii_pos).
person(spouse_s1_a_2_iii_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(95129).
finance(22018).

s2_a(alice_s1_a_2_iii_pos,spouse_s1_a_2_iii_pos,2017).
s63(alice_s1_a_2_iii_pos,2017,95129).

% Test
:- s1_a_iii(95129,22018).
:- halt.
% Text
% Alice is a head of household for the year 2017. Alice's taxable income for the year 2017 is $9560.

% Question
% Alice has to pay $1434 in taxes for the year 2017 under section 1(b)(ii). Contradiction

% Facts
person(alice_s1_b_ii_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(9560).
finance(1434).

s2_b(alice_s1_b_ii_neg,alice_s1_b_ii_neg,2017).
s63(alice_s1_b_ii_neg,2017,9560).

% Test
:- \+ s1_b_ii(9560,1434).
:- halt.
% Text
% Alice is a head of household for the year 2017. Alice's taxable income for the year 2017 is $54775.

% Question
% Alice has to pay $11489 in taxes for the year 2017 under section 1(b)(ii). Entailment

% Facts
person(alice_s1_b_ii_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(54775).
finance(11489).

s2_b(alice_s1_b_ii_pos,alice_s1_b_ii_pos,2017).
s63(alice_s1_b_ii_pos,2017,54775).

% Test
:- s1_b_ii(54775,11489).
:- halt.
% Text
% Alice is a head of household for the year 2017. Alice's taxable income for the year 2017 is $54775.

% Question
% Alice has to pay $11489 in taxes for the year 2017 under section 1(b)(iii). Contradiction

% Facts
person(alice_s1_b_iii_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(54775).
finance(11489).

s2_b(alice_s1_b_iii_neg,alice_s1_b_iii_neg,2017).
s63(alice_s1_b_iii_neg,2017,54775).

% Test
:- \+ s1_b_iii(54775,11489).
:- halt.
% Text
% Alice is a head of household for the year 2017. Alice's taxable income for the year 2017 is $97407.

% Question
% Alice has to pay $24056 in taxes for the year 2017 under section 1(b)(iii). Entailment

% Facts
person(alice_s1_b_iii_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(97407).
finance(24056).

s2_b(alice_s1_b_iii_pos,alice_s1_b_iii_pos,2017).
s63(alice_s1_b_iii_pos,2017,97407).

% Test
:- s1_b_iii(97407,24056).
:- halt.
% Text
% Alice is a head of household for the year 2017. Alice's taxable income for the year 2017 is $97407.

% Question
% Alice has to pay $24056 in taxes for the year 2017 under section 1(b)(iv). Contradiction

% Facts
person(alice_s1_b_iv_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(97407).
finance(24056).

s2_b(alice_s1_b_iv_neg,alice_s1_b_iv_neg,2017).
s63(alice_s1_b_iv_neg,2017,97407).

% Test
:- \+ s1_b_iv(97407,24056).
:- halt.
% Text
% Alice is a head of household for the year 2017. Alice's taxable income for the year 2017 is $194512.

% Question
% Alice has to pay $57509 in taxes for the year 2017 under section 1(b)(iv). Entailment

% Facts
person(alice_s1_b_iv_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(194512).
finance(57509).

s2_b(alice_s1_b_iv_pos,alice_s1_b_iv_pos,2017).
s63(alice_s1_b_iv_pos,2017,194512).

% Test
:- s1_b_iv(194512,57509).
:- halt.
% Text
% Alice is a head of household for the year 2017. Alice's taxable income for the year 2017 is $194512.

% Question
% Alice has to pay $57509 in taxes for the year 2017 under section 1(b)(v). Contradiction

% Facts
person(alice_s1_b_v_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(194512).
finance(57509).

s2_b(alice_s1_b_v_neg,alice_s1_b_v_neg,2017).
s63(alice_s1_b_v_neg,2017,194512).

% Test
:- \+ s1_b_v(194512,57509).
:- halt.
% Text
% Alice is a head of household for the year 2017. Alice's taxable income for the year 2017 is $1172980.

% Question
% Alice has to pay $442985 in taxes for the year 2017 under section 1(b)(v). Entailment

% Facts
person(alice_s1_b_v_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(1172980).
finance(442985).

s2_b(alice_s1_b_v_pos,alice_s1_b_v_pos,2017).
s63(alice_s1_b_v_pos,2017,1172980).

% Test
:- s1_b_v(1172980,442985).
:- halt.
% Text
% Alice's taxable income for the year 2017 is $718791. In 2017, Alice is not married, is not a surviving spouse, and is not a head of household.

% Question
% Alice has to pay $265413 in taxes for the year 2017 under section 1(c)(i). Contradiction

% Facts
person(alice_s1_c_i_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(718791).
finance(265413).

s63(alice_s1_c_i_neg,2017,718791).

% Test
:- \+ s1_c_i(718791,265413).
:- halt.
% Text
% Alice's taxable income for the year 2017 is $7748. In 2017, Alice is not married, is not a surviving spouse, and is not a head of household.

% Question
% Alice has to pay $1162 in taxes for the year 2017 under section 1(c)(i). Entailment

% Facts
person(alice_s1_c_i_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(7748).
finance(1162).

s63(alice_s1_c_i_pos,2017,7748).

% Test
:- s1_c_i(7748,1162).
:- halt.
% Text
% Alice's taxable income for the year 2017 is $7748. Alice is not married, is not a surviving spouse, and is not a head of household in 2017.

% Question
% Alice has to pay $1162 in taxes for the year 2017 under section 1(c)(ii). Contradiction

% Facts
person(alice_s1_c_ii_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(7748).
finance(1162).

s63(alice_s1_c_ii_neg,2017,7748).

% Test
:- \+ s1_c_ii(7748,1162).
:- halt.
% Text
% Alice's taxable income for the year 2017 is $22895. Alice is not married, is not a surviving spouse, and is not a head of household in 2017.

% Question
% Alice has to pay $3538 in taxes for the year 2017 under section 1(c)(ii). Entailment

% Facts
person(alice_s1_c_ii_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(22895).
finance(3538).

s63(alice_s1_c_ii_pos,2017,22895).

% Test
:- s1_c_ii(22895,3538).
:- halt.
% Text
% Alice's taxable income for the year 2017 is $102268. In 2017, Alice is not married, is not a surviving spouse, and is not a head of household.

% Question
% Alice has to pay $27225 in taxes for the year 2017 under section 1(c)(iv). Contradiction

% Facts
person(alice_s1_c_iv_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(102268).
finance(27225).

s63(alice_s1_c_iv_neg,2017,102268).

% Test
:- \+ s1_c_iv(102268,27225).
:- halt.
% Text
% Alice's taxable income for the year 2017 is $210204. In 2017, Alice is not married, is not a surviving spouse, and is not a head of household.

% Question
% Alice has to pay $65445 in taxes for the year 2017 under section 1(c)(iv). Entailment

% Facts
person(alice_s1_c_iv_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(210204).
finance(65445).

s63(alice_s1_c_iv_pos,2017,210204).

% Test
:- s1_c_iv(210204,65445).
:- halt.
% Text
% Alice's taxable income for the year 2017 is $210204. Alice is not married, is not a surviving spouse, and is not a head of household in 2017.

% Question
% Alice has to pay $65445 in taxes for the year 2017 under section 1(c)(v). Contradiction

% Facts
person(alice_s1_c_v_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(210204).
finance(65445).

s63(alice_s1_c_v_neg,2017,210204).

% Test
:- \+ s1_c_v(210204,65445).
:- halt.
% Text
% Alice's taxable income for the year 2017 is $718791. Alice is not married, is not a surviving spouse, and is not a head of household in 2017.

% Question
% Alice has to pay $265413 in taxes for the year 2017 under section 1(c)(v). Entailment

% Facts
person(alice_s1_c_v_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(718791).
finance(265413).

s63(alice_s1_c_v_pos,2017,718791).

% Test
:- s1_c_v(718791,265413).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice's taxable income for the year 2017 is $6662. Alice files a separate return.

% Question
% Alice has to pay $999 in taxes for the year 2017 under section 1(d)(iii). Contradiction

% Facts
person(alice_s1_d_iii_neg).
person(spouse_s1_d_iii_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(6662).
finance(999).

marriage_(alice_and_spouse_s1_d_iii_neg).
s7703(alice_s1_d_iii_neg,spouse_s1_d_iii_neg,alice_and_spouse_s1_d_iii_neg,2017).
s63(alice_s1_d_iii_neg,2017,6662).

% Test
:- \+ s1_d_iii(6662,999).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice's taxable income for the year 2017 is $67285. Alice files a separate return.

% Question
% Alice has to pay $17123 in taxes for the year 2017 under section 1(d)(iii). Entailment

% Facts
person(alice_s1_d_iii_pos).
person(spouse_s1_d_iii_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(67285).
finance(17123).

marriage_(alice_and_spouse_s1_d_iii_pos).
s7703(alice_s1_d_iii_pos,spouse_s1_d_iii_pos,alice_and_spouse_s1_d_iii_pos,2017).
s63(alice_s1_d_iii_pos,2017,67285).

% Test
:- s1_d_iii(67285,17123).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice's taxable income for the year 2017 is $28864. Alice files a separate return.

% Question
% Alice has to pay $5683 in taxes for the year 2017 under section 1(d)(iv). Contradiction

% Facts
person(alice_s1_d_iv_neg).
person(spouse_s1_d_iv_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(28864).
finance(5683).

marriage_(alice_and_spouse_s1_d_iv_neg).
s7703(alice_s1_d_iv_neg,spouse_s1_d_iv_neg,alice_and_spouse_s1_d_iv_neg,2017).
s63(alice_s1_d_iv_neg,2017,28864).

% Test
:- \+ s1_d_iv(28864,5683).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice's taxable income for the year 2017 is $113580. Alice files a separate return.

% Question
% Alice has to pay $33653 in taxes for the year 2017 under section 1(d)(iv). Entailment

% Facts
person(alice_s1_d_iv_pos).
person(spouse_s1_d_iv_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(113580).
finance(33653).

marriage_(alice_and_spouse_s1_d_iv_pos).
s7703(alice_s1_d_iv_pos,spouse_s1_d_iv_pos,alice_and_spouse_s1_d_iv_pos,2017).
s63(alice_s1_d_iv_pos,2017,113580).

% Test
:- s1_d_iv(113580,33653).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice's taxable income for the year 2017 is $554313. Alice files a separate return.

% Question
% Alice has to pay $20772 in taxes for the year 2017 under section 1(d)(v). Contradiction

% Facts
person(alice_s1_d_v_neg).
person(spouse_s1_d_v_neg).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(554313).
finance(20772).

marriage_(alice_and_spouse_s1_d_v_neg).
s7703(alice_s1_d_v_neg,spouse_s1_d_v_neg,alice_and_spouse_s1_d_v_neg,2017).
s63(alice_s1_d_v_neg,2017,554313).

% Test
:- \+ s1_d_v(554313,20772).
:- halt.
% Text
% Alice is married under section 7703 for the year 2017. Alice's taxable income for the year 2017 is $554313. Alice files a separate return.

% Question
% Alice has to pay $207772 in taxes for the year 2017 under section 1(d)(v). Entailment

% Facts
person(alice_s1_d_v_pos).
person(spouse_s1_d_v_pos).
year(2017).
date(d2017_01_01).
date(d2017_12_31).
date_split(d2017_01_01,2017,1,1).
date_split(d2017_12_31,2017,12,31).
finance(554313).
finance(207772).

marriage_(alice_and_spouse_s1_d_v_pos).
s7703(alice_s1_d_v_pos,spouse_s1_d_v_pos,alice_and_spouse_s1_d_v_pos,2017).
s63(alice_s1_d_v_pos,2017,554313).

% Test
:- s1_d_v(554313,207772).
:- halt.

End of examples.

Given the examples that has been shown, you, the system, is asked to provide the ASP code (Facts and Test)
of the following natural language text:

1.
% Text
% Alice is a surviving spouse for the year 2017. Alice's taxable income for the year 2017 is $615572.

% Question
% Alice has to pay $220295 in taxes for the year 2017 under section 1(a)(iv). Contradiction

2.
% Text
% Alice is a surviving spouse for the year 2017. Alice's taxable income for the year 2017 is $236422.

% Question
% Alice has to pay $70640 in taxes for the year 2017 under section 1(a)(iv). Entailment

3.
% Text
% Alice is a head of household for the year 2017. Alice's taxable income for the year 2017 is $1172980.

% Question
% Alice has to pay $442985 in taxes for the year 2017 under section 1(b)(i). Contradiction

4.
% Text
% Alice is a head of household for the year 2017. Alice's taxable income for the year 2017 is $9560.

% Question
% Alice has to pay $1434 in taxes for the year 2017 under section 1(b)(i). Entailment

5.
% Text
% Alice is married under section 7703 for the year 2017. Alice's taxable income for the year 2017 is $67285. Alice files taxes separately in 2017.

% Question
% Alice has to pay $17123 in taxes for the year 2017 under section 1(d)(i). Contradiction

6.
% Text
% Alice is married under section 7703 for the year 2017. Alice's taxable income for the year 2017 is $6662. Alice files taxes separately in 2017.

% Question
% Alice has to pay $999 in taxes for the year 2017 under section 1(d)(i). Entailment

7.
% Text
% Alice's taxable income for the year 2017 is $22895. Alice is not married, is not a surviving spouse, and is not a head of household in 2017.

% Question
% Alice has to pay $3538 in taxes for the year 2017 under section 1(c)(iii). Contradiction

"""

llm_manager.chat_completion(prompt)
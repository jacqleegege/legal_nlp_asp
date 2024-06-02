import llm_managers as llm

llm_manager = llm.HuggingFaceLlmManager( model_name= "mistralai/Mistral-7B-Instruct-v0.2")

prompt = """You are a system responsible with translating natural language legal cases to its ASP form
You need to follow the format of the given examples. Here are some examples to learn from:

EXAMPLE 1:
% Text
% Alice has paid wages of $3200 to Bob for work done from Feb 1st, 2017 to Sep 2nd, 2017. Bob has paid wages of $4500 to Alice for work done from Apr 1st, 2017 to Sep 2nd, 2018.

% Question
% Section 3306(a)(1)(A) make Alice an employer for the year 2019. Contradiction

% Facts
person(alice_s3306_a_1_A_neg).
person(bob_s3306_a_1_A_neg).
finance(3200).
finance(4500).

date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_04_01).
date_split(d2017_04_01, 2017, 4, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2018).
date(d2018_09_02).
date_split(d2018_09_02, 2018, 9, 2).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

s3306_b(3200,3200,bob_works_s3306_a_1_A_neg,alice_s3306_a_1_A_neg,bob_s3306_a_1_A_neg,alice_s3306_a_1_A_neg,bob_s3306_a_1_A_neg,cash).
start_(bob_works_s3306_a_1_A_neg,d2017_02_01).
end_(bob_works_s3306_a_1_A_neg,d2017_09_02).
s3306_b(4500,4500,alice_works_s3306_a_1_A_neg,bob_s3306_a_1_A_neg,alice_s3306_a_1_A_neg,bob_s3306_a_1_A_neg,alice_s3306_a_1_A_neg,cash).
start_(alice_works_s3306_a_1_A_neg,d2017_04_01).
end_(alice_works_s3306_a_1_A_neg,d2018_09_02).

% Test
:- \+ s3306_a_1_A(alice_s3306_a_1_A_neg,2019,3200).

EXAMPLE 2:
% Text
% Alice has paid wages of $3200 to Bob for domestic service done from Feb 1st, 2017 to Sep 2nd, 2017. In 2018, Bob has paid wages of $4500 to Alice for work done from Apr 1st, 2017 to Sep 2nd, 2018.

% Question
% Bob is an employer under section 3306(a)(1) for the year 2018. Entailment

% Facts
person(alice_s3306_a_1_pos).
person(bob_s3306_a_1_pos).

year(2017).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_09_02).
date_split(d2019_09_02, 2019, 9, 2).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

year(2018).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_09_02).
date_split(d2018_09_02, 2018, 9, 2).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

finance(3200).
finance(4500).

service_(alice_employer_s3306_a_1_pos).
patient_(alice_employer_s3306_a_1_pos,alice_s3306_a_1_pos).
agent_(alice_employer_s3306_a_1_pos,bob_s3306_a_1_pos).
start_(alice_employer_s3306_a_1_pos,d2017_02_01).
end_(alice_employer_s3306_a_1_pos,d2017_09_02).
purpose_(alice_employer_s3306_a_1_pos,domestic_service).
payment_(alice_pays_s3306_a_1_pos).
agent_(alice_pays_s3306_a_1_pos,alice_s3306_a_1_pos).
patient_(alice_pays_s3306_a_1_pos,bob_s3306_a_1_pos).
start_(alice_pays_s3306_a_1_pos,d2019_09_02).
purpose_(alice_pays_s3306_a_1_pos,alice_employer_s3306_a_1_pos).
amount_(alice_pays_s3306_a_1_pos,3200).
s3306_b(3200,alice_pays_s3306_a_1_pos,alice_employer_s3306_a_1_pos,alice_s3306_a_1_pos,bob_s3306_a_1_pos,alice_s3306_a_1_pos,bob_s3306_a_1_pos,cash).
service_(bob_employer_s3306_a_1_pos).
patient_(bob_employer_s3306_a_1_pos,bob_s3306_a_1_pos).
agent_(bob_employer_s3306_a_1_pos,alice_s3306_a_1_pos).
start_(bob_employer_s3306_a_1_pos,d2017_02_01).
end_(bob_employer_s3306_a_1_pos,d2017_09_02).
payment_(bob_pays_s3306_a_1_pos).
agent_(bob_pays_s3306_a_1_pos,bob_s3306_a_1_pos).
patient_(bob_pays_s3306_a_1_pos,alice_s3306_a_1_pos).
start_(bob_pays_s3306_a_1_pos,d2018_09_02).
end_(bob_pays_s3306_a_1_pos,d2018_09_02).
purpose_(bob_pays_s3306_a_1_pos,bob_employer_s3306_a_1_pos).
amount_(bob_pays_s3306_a_1_pos,4500).
s3306_b(4500,bob_pays_s3306_a_1_pos,bob_employer_s3306_a_1_pos,bob_s3306_a_1_pos,alice_s3306_a_1_pos,bob_s3306_a_1_pos,alice_s3306_a_1_pos,cash).

% Test
:- s3306_a_1(bob_s3306_a_1_pos,2018).

END OF EXAMPLES

Given the examples that has been shown, you, the system, is asked to provide the ASP code (Facts and Test)
of the following natural language text:

1.
% Text
% Alice has paid $45252 to Bob for work done in the year 2017. In 2017, Alice has also paid $9832 into a retirement fund for Bob, and $5322 into health insurance for Charlie, who is Alice's father and has retired in 2016.

% Question
% Section 3306(b)(2)(A) applies to the payment Alice made to Bob for the year 2017. Contradiction

2.
% Text
% Alice has employed Bob from Jan 2nd, 2011 to Oct 10, 2019. On Oct 10, 2019 Bob was diagnosed as disabled and retired. Alice paid Bob $12980 because she had to terminate their contract due to Bob's disability.

% Question
% Section 3306(b)(10)(A) applies to the payment of $12980 that Alice made in 2019. Entailment

3.
% Text
% Alice was paid $3200 in 2017 for services performed for Johns Hopkins University. Alice was enrolled as a physics major at Johns Hopkins University and attending classes from August 29, 2015 to May 30th, 2019.

% Question
% Section 3306(c)(13) applies to Alice's employment situation in 2017. Contradiction

4.
% Text
% Alice has paid $3200 to Bob for work done from Feb 1st, 2017 to Sep 2nd, 2017, in Baltimore, Maryland, USA.

% Question
% Section 3306(c)(A) applies to Alice employing Bob for the year 2017. Entailment

5.
% Text
% Alice and Bob got married on April 5th, 2012. Alice and Bob were legally separated under a decree of divorce on September 16th, 2017.

% Question
% Section 7703(a)(2) applies to Alice for the year 2012. Contradiction

"""

llm_manager.chat_completion(prompt,print_result=True, max_new_tokens=2000)

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

EXAMPLE 3:
% Text
% Over the year 2018, Alice has paid $2325 in cash to Bob for walking her dog.

% Question
% Section 3306(b) applies to the money paid by Alice to Bob for the year 2018. Entailment

% Facts
person(alice_s3306_b_pos).
person(bob_s3306_b_pos).

year(2018).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

finance(2325).
medium(cash).

service_(alice_employer_s3306_b_pos).
patient_(alice_employer_s3306_b_pos,alice_s3306_b_pos).
agent_(alice_employer_s3306_b_pos,bob_s3306_b_pos).
start_(alice_employer_s3306_b_pos,d2018_01_01).
end_(alice_employer_s3306_b_pos,d2018_12_31).
purpose_(alice_employer_s3306_b_pos,walking_her_dog).
payment_(alice_pays_s3306_b_pos).
agent_(alice_pays_s3306_b_pos,alice_s3306_b_pos).
patient_(alice_pays_s3306_b_pos,bob_s3306_b_pos).
start_(alice_pays_s3306_b_pos,d2018_01_01).
end_(alice_pays_s3306_b_pos,d2018_12_31).
purpose_(alice_pays_s3306_b_pos,alice_employer_s3306_b_pos).
amount_(alice_pays_s3306_b_pos,2325).
means_(alice_pays_s3306_b_pos,cash).

% Test
:- s3306_b(2325,alice_pays_s3306_b_pos,alice_employer_s3306_b_pos,alice_s3306_b_pos,bob_s3306_b_pos,alice_s3306_b_pos,bob_s3306_b_pos,cash).

EXAMPLE 4:
% Text
% Alice and Bob got married on April 5th, 2012. Bob died September 16th, 2017.

% Question
% Section 7703(a)(1) applies to Alice for the year 2018. Contradiction

% Facts
person(alice_s7703_a_1_neg).
person(bob_s7703_a_1_neg).

year(2012).
date(d2012_01_01).
date_split(d2012_01_01, 2012, 1, 1).
date(d2012_04_05).
date_split(d2012_04_05, 2012, 4, 5).
date(d2012_12_31).
date_split(d2012_12_31, 2012, 12, 31).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_09_16).
date_split(d2017_09_16, 2017, 9, 16).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2018).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

marriage_(alice_and_bob_s7703_a_1_neg).
agent_(alice_and_bob_s7703_a_1_neg,alice_s7703_a_1_neg).
agent_(alice_and_bob_s7703_a_1_neg,bob_s7703_a_1_neg).
start_(alice_and_bob_s7703_a_1_neg,d2012_04_05).
death_(bob_dies_s7703_a_1_neg).
agent_(bob_dies_s7703_a_1_neg,bob_s7703_a_1_neg).
start_(bob_dies_s7703_a_1_neg,d2017_09_16).

% Test
:- \+ s7703_a_1(alice_s7703_a_1_neg,bob_s7703_a_1_neg,alice_and_bob_s7703_a_1_neg,d2017_09_16,2018).

EXAMPLE 5:
% Text
% Alice and Bob got married on April 5th, 2012. Alice and Bob were legally separated under a decree of divorce on September 16th, 2017.

% Question
% Section 7703(a)(2) applies to Alice for the year 2018. Entailment

% Facts
person(alice_s7703_a_2_pos).
person(bob_s7703_a_2_pos).

year(2012).
date(d2012_01_01).
date_split(d2012_01_01, 2012, 1, 1).
date(d2012_04_05).
date_split(d2012_04_05, 2012, 4, 5).
date(d2012_12_31).
date_split(d2012_12_31, 2012, 12, 31).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_09_16).
date_split(d2017_09_16, 2017, 9, 16).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2018).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

marriage_(alice_and_bob_s7703_a_2_pos).
agent_(alice_and_bob_s7703_a_2_pos,alice_s7703_a_2_pos).
agent_(alice_and_bob_s7703_a_2_pos,bob_s7703_a_2_pos).
start_(alice_and_bob_s7703_a_2_pos,d2012_04_05).
legal_separation_(alice_and_bob_divorce_s7703_a_2_pos).
patient_(alice_and_bob_divorce_s7703_a_2_pos,alice_and_bob_s7703_a_2_pos).
agent_(alice_and_bob_divorce_s7703_a_2_pos,decree_of_divorce).
start_(alice_and_bob_divorce_s7703_a_2_pos,d2017_09_16).

% Test
:- s7703_a_2(alice_s7703_a_2_pos,bob_s7703_a_2_pos,alice_and_bob_s7703_a_2_pos,alice_and_bob_divorce_s7703_a_2_pos,2018).

EXAMPLE 6:
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice died on July 9th, 2014. Bob married Charlie on September 14th, 2015.

% Question
% Section 2(a)(2)(A) applies to Bob in 2015. Entailment

% Facts
person(alice_s2_a_2_A_pos).
person(bob_s2_a_2_A_pos).
person(charlie_s2_a_2_A_pos).

year(1992).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).

year(2014).
date(d2014_07_09).
date_split(d2014_07_09,2014,7,9).
date(d2014_01_01).
date_split(d2014_01_01,2014,1,1).
date(d2014_12_31).
date_split(d2014_12_31,2014,12,31).

year(2015).
date(d2015_09_14).
date_split(d2015_09_14,2015,9,14).
date(d2015_01_01).
date_split(d2015_01_01,2015,1,1).
date(d2015_12_31).
date_split(d2015_12_31,2015,12,31).

marriage_(alice_and_bob_s2_a_2_A_pos).
agent_(alice_and_bob_s2_a_2_A_pos,alice_s2_a_2_A_pos).
agent_(alice_and_bob_s2_a_2_A_pos,bob_s2_a_2_A_pos).
start_(alice_and_bob_s2_a_2_A_pos,d1992_02_03).
death_(alice_dies_s2_a_2_A_pos).
agent_(alice_dies_s2_a_2_A_pos,alice_s2_a_2_A_pos).
start_(alice_dies_s2_a_2_A_pos,d2014_07_09).
end_(alice_dies_s2_a_2_A_pos,d2014_07_09).
marriage_(bob_and_charlie_s2_a_2_A_pos).
agent_(bob_and_charlie_s2_a_2_A_pos,charlie_s2_a_2_A_pos).
agent_(bob_and_charlie_s2_a_2_A_pos,bob_s2_a_2_A_pos).
start_(bob_and_charlie_s2_a_2_A_pos,d2015_09_14).

% Test
:- s2_a_2_A(bob_s2_a_2_A_pos,bob_and_charlie_s2_a_2_A_pos,alice_and_bob_s2_a_2_A_pos,d2015_09_14,2015).

EXAMPLE 7:
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice was a nonresident alien until July 9th, 2014.

% Question
% Section 2(b)(2)(B) applies to Bob in 2015. Contradiction

% Facts
person(alice_s2_b_2_B_neg).
person(bob_s2_b_2_B_neg).

year(1992).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).

year(2014).
date(d2014_07_09).
date_split(d2014_07_09,2014,7,9).
date(d2014_01_01).
date_split(d2014_01_01,2014,1,1).
date(d2014_12_31).
date_split(d2014_12_31,2014,12,31).

year(2015).

marriage_(alice_and_bob_s2_b_2_B_neg).
agent_(alice_and_bob_s2_b_2_B_neg,alice_s2_b_2_B_neg).
agent_(alice_and_bob_s2_b_2_B_neg,bob_s2_b_2_B_neg).
start_(alice_and_bob_s2_b_2_B_neg,d1992_02_03).
nonresident_alien_(alice_is_a_nra_s2_b_2_B_neg).
agent_(alice_is_a_nra_s2_b_2_B_neg,alice_s2_b_2_B_neg).
end_(alice_is_a_nra_s2_b_2_B_neg,d2014_07_09).

% Test
:- \+ s2_b_2_B(bob_s2_b_2_B_neg,alice_s2_b_2_B_neg,2015).

EXAMPLE 8:
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017. Alice is entitled to an additional standard deduction of $600 each for herself and for Bob, under section 63(f)(1)(A) and 63(f)(1)(B), respectively.

% Question
% Under section 63(c)(3), Alice's additional standard deduction in 2017 is equal to $300. Contradiction

% Facts
person(alice_s63_c_3_neg).
person(bob_s63_c_3_neg).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03,2017,2,3).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).
finance(300).

payment_(alice_is_paid_s63_c_3_neg).
patient_(alice_is_paid_s63_c_3_neg,alice_s63_c_3_neg).
start_(alice_is_paid_s63_c_3_neg,d2017_12_31).
amount_(alice_is_paid_s63_c_3_neg,33200).
marriage_(alice_and_bob_s63_c_3_neg).
agent_(alice_and_bob_s63_c_3_neg,alice_s63_c_3_neg).
agent_(alice_and_bob_s63_c_3_neg,bob_s63_c_3_neg).
start_(alice_and_bob_s63_c_3_neg,d2017_02_03).
s63_f_1_A(alice_s63_c_3_neg,2017).
s63_f_1_B(alice_s63_c_3_neg,bob_s63_c_3_neg,2017).

% Test
:- \+ s63_c_3(alice_s63_c_3_neg,300,2017).

EXAMPLE 9:
% Text
% In 2017, Alice was paid $33200. She is allowed a deduction under $1200 for the year 2017 for donating cash to charity.

% Question
% Alice's deduction for 2017 falls under section 63(d). Entailment

% Facts
person(alice_s63_d_pos).
finance(33200).
finance(1200).

year(2017).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

payment_(alice_is_paid_s63_d_pos).
patient_(alice_is_paid_s63_d_pos,alice_s63_d_pos).
start_(alice_is_paid_s63_d_pos,d2017_12_31).
amount_(alice_is_paid_s63_d_pos,33200).
deduction_(deduction_alice_2017_s63_d_pos).
agent_(deduction_alice_2017_s63_d_pos,alice_s63_d_pos).
start_(deduction_alice_2017_s63_d_pos,d2017_12_31).
amount_(deduction_alice_2017_s63_d_pos,1200).

% Test
:- s63_d(alice_s63_d_pos,1200,1200,2017).

EXAMPLE 10:
% Text
% In 2016, Alice's income was $567192. Alice is a surviving spouse for the year 2016.

% Question
% Under section 68(b)(1)(B), Alice's applicable amount for 2016 is equal to $275000. Contradiction

% Facts
person(alice_s68_b_1_B_neg).
person(spouse_s68_b_1_B_neg).
finance(567192).
finance(275000).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

income_(alice_is_paid_s68_b_1_B_neg).
agent_(alice_is_paid_s68_b_1_B_neg,alice_s68_b_1_B_neg).
start_(alice_is_paid_s68_b_1_B_neg,d2016_12_31).
amount_(alice_is_paid_s68_b_1_B_neg,567192).
s2_a(alice_s68_b_1_B_neg,spouse_s68_b_1_B_neg,2016).

% Test
:- \+ s68_b_1_B(alice_s68_b_1_B_neg,275000,2016).

EXAMPLE 11:
% Text
% Alice's income in 2015 was $260932. For 2015, Alice received one exemption of $2000 under section 151(c). Alice's applicable percentage under section 151(d)(3)(B) is equal to 10%.

% Question
% Under section 151(d)(3)(A), Alice's exemption amount is reduced to $1800. Entailment

% Facts
person(alice_s151_d_3_A_pos).

finance(260932).
finance(250000).
finance(10).
finance(2000).
finance(1800).


year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

income_(alice_makes_money_s151_d_3_A_pos).
agent_(alice_makes_money_s151_d_3_A_pos,alice_s151_d_3_A_pos).
amount_(alice_makes_money_s151_d_3_A_pos,260932).
start_(alice_makes_money_s151_d_3_A_pos,d2015_01_01).
end_(alice_makes_money_s151_d_3_A_pos,d2015_12_31).
s151_c(alice_s151_d_3_A_pos,alice_s151_d_3_A_pos,2000,2015).

% Test
:- s151_d_3_A(alice_s151_d_3_A_pos,260932,250000,10,2000,1800,2015)

EXAMPLE 12:
% Text
% Alice has a son, Bob. From September 1st, 2015 to November 3rd, 2019, Alice and Bob lived in the same home. Bob married Charlie on October 23rd, 2018. Bob and Charlie file separate returns.

% Question
% Section 152(c)(1)(E) applies to Bob for the year 2019. Entailment

% Facts
person(alice_s152_c_1_E_pos).
person(bob_s152_c_1_E_pos).
person(charlie_s152_c_1_E_pos).

year(2015).
date(d2015_09_01).
date_split(d2015_09_01, 2015, 9, 1).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

year(2018).
date(d2018_10_23).
date_split(d2018_10_23, 2018, 10, 23).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

year(2019).
date(d2019_11_03).
date_split(d2019_11_03, 2019, 11, 3).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

son_(bob_is_son_s152_c_1_E_pos).
agent_(bob_is_son_s152_c_1_E_pos,bob_s152_c_1_E_pos).
patient_(bob_is_son_s152_c_1_E_pos,alice_s152_c_1_E_pos).
residence_(alice_and_bob_s152_c_1_E_pos).
agent_(alice_and_bob_s152_c_1_E_pos,alice_s152_c_1_E_pos).
agent_(alice_and_bob_s152_c_1_E_pos,bob_s152_c_1_E_pos).
patient_(alice_and_bob_s152_c_1_E_pos,home_s152_c_1_E_pos).
start_(alice_and_bob_s152_c_1_E_pos,d2015_09_01).
end_(alice_and_bob_s152_c_1_E_pos,d2019_11_03).
marriage_(bob_and_charlie_s152_c_1_E_pos).
agent_(bob_and_charlie_s152_c_1_E_pos,bob_s152_c_1_E_pos).
agent_(bob_and_charlie_s152_c_1_E_pos,charlie_s152_c_1_E_pos).
start_(bob_and_charlie_s152_c_1_E_pos,d2018_10_23).

% Test
:- s152_c_1_E(bob_s152_c_1_E_pos,charlie_s152_c_1_E_pos,2019).

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
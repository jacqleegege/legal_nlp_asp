import llm_managers as llm

llm_manager = llm.HuggingFaceLlmManager( model_name= "mistralai/Mistral-7B-Instruct-v0.2")
# llm_manager = llm.HuggingFaceLlmManager( model_name= "meta-llama/Llama-2-7b-chat-hf")

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
% Alice's income in 2015 is $100000. She gets one exemption of $2000 for the year 2015 under section 151(c). Alice is not married.

% Question
% Alice's total exemption for 2015 under section 151(a) is equal to $6000. Contradiction

% Facts
person(alice_s151_a_neg).
person(bob_s151_a_neg).
finance(100000).
finance(2000).
finance(6000).


year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

income_(alice_makes_money_s151_a_neg).
agent_(alice_makes_money_s151_a_neg,alice_s151_a_neg).
start_(alice_makes_money_s151_a_neg,d2015_01_01).
end_(alice_makes_money_s151_a_neg,d2015_12_31).
amount_(alice_makes_money_s151_a_neg,100000).
s151_c(alice_s151_a_neg,bob_s151_a_neg,2000,2015).


% Test
:- \+ s151_a(alice_s151_a_neg,6000,2015).
:- halt.
% Text
% Alice's income in 2015 is $100000. She gets one exemption of $2000 for the year 2015 under section 151(c). Alice is not married.

% Question
% Alice's total exemption for 2015 under section 151(a) is equal to $4000. Entailment

% Facts
person(alice_s151_a_pos).
person(bob_s151_a_pos).
finance(100000).
finance(2000).
finance(4000).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

income_(alice_makes_money_s151_a_pos).
agent_(alice_makes_money_s151_a_pos,alice_s151_a_pos).
start_(alice_makes_money_s151_a_pos,d2015_01_01).
end_(alice_makes_money_s151_a_pos,d2015_12_31).
amount_(alice_makes_money_s151_a_pos,100000).
s151_c(alice_s151_a_pos,bob_s151_a_pos,2000,2015).

% Test
:- s151_a(alice_s151_a_pos,4000,2015).
:- halt.
% Text
% Alice and Bob have been married since 2 Feb 2015. Bob has no income for 2015. Alice and Bob file their taxes jointly for 2015.

% Question
% Alice can receive an exemption for Bob under section 151(b) for the year 2015. Contradiction

% Facts
person(alice_s151_b_neg).
person(bob_s151_b_neg).
finance(2000).

year(2015).
date(d2015_02_02).
date_split(d2015_02_02, 2015, 2, 2).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

marriage_(alice_and_bob_s151_b_neg).
agent_(alice_and_bob_s151_b_neg,alice_s151_b_neg).
agent_(alice_and_bob_s151_b_neg,bob_s151_b_neg).
start_(alice_and_bob_s151_b_neg,d2015_02_02).
joint_return_(alice_and_bob_joint_return_s151_b_neg).
agent_(alice_and_bob_joint_return_s151_b_neg,alice_s151_b_neg).
agent_(alice_and_bob_joint_return_s151_b_neg,bob_s151_b_neg).
start_(alice_and_bob_joint_return_s151_b_neg,d2015_01_01).
end_(alice_and_bob_joint_return_s151_b_neg,d2015_12_31).

% Test
:- \+ s151_b(alice_s151_b_neg,bob_s151_b_neg,2000,2015).
:- halt.
% Text
% Alice and Bob have been married since 2 Feb 2015. Bob has no income for 2015.
%
% Question
% Alice can receive an exemption for Bob under section 151(b) for the year 2015. Entailment

% Facts

person(alice_s151_b_pos).
person(bob_s151_b_pos).
person(2000).

year(2015).
date(d2015_02_02).
date_split(d2015_02_02, 2015, 2, 2).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

marriage_(alice_and_bob_s151_b_pos).
agent_(alice_and_bob_s151_b_pos,alice_s151_b_pos).
agent_(alice_and_bob_s151_b_pos,bob_s151_b_pos).
start_(alice_and_bob_s151_b_pos,d2015_02_02).

% Test
:- s151_b(alice_s151_b_pos,bob_s151_b_pos,2000,2015).
:- halt.
% Text
% Alice and Bob have been married since 2 Feb 2015. Charlie counts as Alice's dependent under section 152(c)(1) for 2015.

% Question
% Alice can claim an exemption with Bob as the dependent for 2015 under section 151(c). Contradiction

% Facts
person(alice_s151_c_neg).
person(bob_s151_c_neg).
person(charlie_s151_c_neg).

finance(2000).

year(2015).
date(d2015_02_02).
date_split(d2015_02_02, 2015, 2, 2).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

marriage_(alice_and_bob_s151_c_neg).
agent_(alice_and_bob_s151_c_neg,alice_s151_c_neg).
agent_(alice_and_bob_s151_c_neg,bob_s151_c_neg).
start_(alice_and_bob_s151_c_neg,d2015_02_02).
s152_c_1(charlie_s151_c_neg,alice_s151_c_neg,2015).

% Test
:- \+ s151_c(alice_s151_c_neg,bob_s151_c_neg,2000,2015).
:- halt.
% Text
% Alice and Charlie have been married since 2 Feb 2015. Bob counts as Alice's dependent under section 152(c)(1) for 2015.

% Question
% Alice can claim an exemption with Bob the dependent for 2015 under section 151(c). Entailment

% Facts
person(alice_s151_c_pos).
person(bob_s151_c_pos).
person(charlie_s151_c_pos).
finance(2000).

year(2015).
date(d2015_02_02).
date_split(d2015_02_02, 2015, 2, 2).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

marriage_(alice_and_charlie_s151_c_pos).
agent_(alice_and_charlie_s151_c_pos,alice_s151_c_pos).
agent_(alice_and_charlie_s151_c_pos,charlie_s151_c_pos).
start_(alice_and_charlie_s151_c_pos,d2015_02_02).
s152_c_1(bob_s151_c_pos,alice_s151_c_pos,2015).

% Test
:- s151_c(alice_s151_c_pos,bob_s151_c_pos,2000,2015).
:- halt.
% Text
% Alice is entitled to an exemption under section 151(d) for Bob for the year 2015.

% Question
% Under section 151(d)(2), Bob's exemption amount for the year 2015 is equal to $2000. Contradiction

% Facts
person(alice_s151_d_2_neg).
person(bob_s151_d_2_neg).
finance(2000).


year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

s151_d(alice_s151_d_2_neg,bob_s151_d_2_neg,2000,2015).

% Test
:- \+ s151_d_2(bob_s151_d_2_neg,alice_s151_d_2_neg,2000,2015).
:- halt.
% Text
% Alice is entitled to an exemption under section 151(c) for Bob for the year 2015.

% Question
% Under section 151(d)(2), Bob's exemption amount for the year 2015 is equal to $0. Entailment

% Facts
person(alice_s151_d_2_pos).
person(bob_s151_d_2_pos).
finance(0).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

s151_c_applies(alice_s151_d_2_pos,bob_s151_d_2_pos,2015).

% Test
:- s151_d_2(bob_s151_d_2_pos,alice_s151_d_2_pos,0,2015).
:- halt.
% Text
% Alice's income in 2015 is $395276. The applicable amount according to section 68(b) is $250000.
%
% Question
% Under section 151(d)(3)(B), the applicable percentage for Alice for 2015 is equal to 118. Contradiction

% Facts
person(alice_s151_d_3_B_neg).

finance(395276).
finance(250000).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

income_(alice_makes_money_s151_d_3_B_neg).
agent_(alice_makes_money_s151_d_3_B_neg,alice_s151_d_3_B_neg).
amount_(alice_makes_money_s151_d_3_B_neg,395276).
start_(alice_makes_money_s151_d_3_B_neg,d2015_01_01).
end_(alice_makes_money_s151_d_3_B_neg,d2015_12_31).
s68_b(alice_s151_d_3_B_neg,2015,250000).

% Test
:- \+ s151_d_3_B(118,alice_s151_d_3_B_neg,395276,2015,250000).
:- halt.
% Text
% Alice's income in 2015 is $276932. Alice is not married. The applicable amount according to section 68(b) is $250000.

% Question
% Under section 151(d)(3)(B), the applicable percentage for Alice for 2015 is equal to 22. Entailment

% Facts
person(alice_s151_d_3_B_pos).

finance(276932).
finance(250000).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

income_(alice_makes_money_s151_d_3_B_pos).
agent_(alice_makes_money_s151_d_3_B_pos,alice_s151_d_3_B_pos).
amount_(alice_makes_money_s151_d_3_B_pos,276932).
start_(alice_makes_money_s151_d_3_B_pos,d2015_01_01).
end_(alice_makes_money_s151_d_3_B_pos,d2015_12_31).
s68_b(alice_s151_d_3_B_pos,2015,250000).

% Test
:- s151_d_3_B(22,alice_s151_d_3_B_pos,276932,2015,250000).
:- halt.
% Text
% Alice has a son, Bob, who satisfies section 152(c)(1) for the year 2015. Bob has a son, Charlie, who satisfies section 152(c)(1) for the year 2015.

% Question
% Section 152(b)(1) applies to Alice for the year 2015. Contradiction

% Facts
person(alice_s152_b_1_neg).
person(bob_s152_b_1_neg).
person(charlie_s152_b_1_neg).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

s152_c_1(bob_s152_b_1_neg,alice_s152_b_1_neg,2015).
s152_c_1(charlie_s152_b_1_neg,bob_s152_b_1_neg,2015).

% Test
:- \+ s152_b_1(alice_s152_b_1_neg,bob_s152_b_1_neg,2015).
:- halt.
% Text
% Alice has a son, Bob, who satisfies section 152(c)(1) for the year 2015. Bob has a son, Charlie, who satisfies section 152(c)(1) for the year 2015.

% Question
% Section 152(b)(1) applies to Bob for the year 2015. Entailment

% Facts
person(alice_s152_b_1_pos).
person(bob_s152_b_1_pos).
person(charlie_s152_b_1_pos).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

s152_c_1(bob_s152_b_1_pos,alice_s152_b_1_pos,2015).
s152_c_1(charlie_s152_b_1_pos,bob_s152_b_1_pos,2015).

% Test
:- s152_b_1(bob_s152_b_1_pos,charlie_s152_b_1_pos,2015).
:- halt.
% Text
% Alice and Bob got married on Jan 1st, 2015. Alice and Bob file separately in 2015.

% Question
% Section 152(b)(2) applies to Alice the year 2015. Contradiction

% Facts
person(alice_s152_b_2_neg).
person(bob_s152_b_2_neg).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

marriage_(alice_and_bob_s152_b_2_neg).
agent_(alice_and_bob_s152_b_2_neg,alice_s152_b_2_neg).
agent_(alice_and_bob_s152_b_2_neg,bob_s152_b_2_neg).
start_(alice_and_bob_s152_b_2_neg,d2015_01_01).
joint_return_(random_joint_return).

% Test
:- \+ s152_b_2(alice_s152_b_2_neg,random_joint_return,bob_s152_b_2_neg,2015).
:- halt.
% Text
% Alice and Bob got married on Jan 1st, 2015. They file a joint return for the year 2015.

% Question
% Section 152(b)(2) applies to Alice for the year 2015. Entailment

% Facts
person(alice_s152_b_2_pos).
person(bob_s152_b_2_pos).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

marriage_(alice_and_bob_s152_b_2_pos).
agent_(alice_and_bob_s152_b_2_pos,alice_s152_b_2_pos).
agent_(alice_and_bob_s152_b_2_pos,bob_s152_b_2_pos).
start_(alice_and_bob_s152_b_2_pos,d2015_01_01).
joint_return_(alice_and_bob_joint_return_s152_b_2_pos).
agent_(alice_and_bob_joint_return_s152_b_2_pos,alice_s152_b_2_pos).
agent_(alice_and_bob_joint_return_s152_b_2_pos,bob_s152_b_2_pos).
start_(alice_and_bob_joint_return_s152_b_2_pos,d2015_01_01).
end_(alice_and_bob_joint_return_s152_b_2_pos,d2015_12_31).

% Test
:- s152_b_2(alice_s152_b_2_pos,alice_and_bob_joint_return_s152_b_2_pos,bob_s152_b_2_pos,2015).
:- halt.
% Text
% Alice has a son, Bob. From September 1st, 2015 to November 3rd, 2019, Alice and Bob lived in the same home.

% Question
% Section 152(c)(1)(B) applies to Bob with Alice as the taxpayer for the year 2015. Contradiction

% Facts
person(alice_s152_c_1_B_neg).
person(bob_s152_c_1_B_neg).

year(2015).
date(d2015_09_01).
date_split(d2015_09_01, 2015, 9, 1).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

year(2019).
date(d2019_11_03).
date_split(d2019_11_03, 2019, 11, 3).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

son_(bob_is_son_s152_c_1_B_neg).
agent_(bob_is_son_s152_c_1_B_neg,bob_s152_c_1_B_neg).
patient_(bob_is_son_s152_c_1_B_neg,alice_s152_c_1_B_neg).
residence_(alice_and_bob_s152_c_1_B_neg).
agent_(alice_and_bob_s152_c_1_B_neg,alice_s152_c_1_B_neg).
agent_(alice_and_bob_s152_c_1_B_neg,bob_s152_c_1_B_neg).
patient_(alice_and_bob_s152_c_1_B_neg,home_s152_c_1_B_neg).
start_(alice_and_bob_s152_c_1_B_neg,d2015_09_01).
end_(alice_and_bob_s152_c_1_B_neg,d2019_11_03).

% Test
:- \+ s152_c_1_B(bob_s152_c_1_B_neg,home_s152_c_1_B_neg,alice_s152_c_1_B_neg,d2015_09_01,"2019-11-03",2015).
:- halt.
% Text
% Alice has a son, Bob. From September 1st, 2015 to November 3rd, 2019, Alice and Bob lived in the same home.

% Question
% Section 152(c)(1)(B) applies to Bob with Alice as the taxpayer for the year 2016. Entailment

% Facts
person(alice_s152_c_1_B_pos).
person(bob_s152_c_1_B_pos).

year(2015).
date(d2015_09_01).
date_split(d2015_09_01, 2015, 9, 1).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

year(2019).
date(d2019_11_03).
date_split(d2019_11_03, 2019, 11, 3).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

son_(bob_is_son_s152_c_1_B_pos).
agent_(bob_is_son_s152_c_1_B_pos,bob_s152_c_1_B_pos).
patient_(bob_is_son_s152_c_1_B_pos,alice_s152_c_1_B_pos).
residence_(alice_and_bob_s152_c_1_B_pos).
agent_(alice_and_bob_s152_c_1_B_pos,alice_s152_c_1_B_pos).
agent_(alice_and_bob_s152_c_1_B_pos,bob_s152_c_1_B_pos).
patient_(alice_and_bob_s152_c_1_B_pos,home_s152_c_1_B_pos).
start_(alice_and_bob_s152_c_1_B_pos,d2015_09_01).
end_(alice_and_bob_s152_c_1_B_pos,d2019_11_03).

% Test
:- s152_c_1_B(bob_s152_c_1_B_pos,home_s152_c_1_B_pos,alice_s152_c_1_B_pos,d2015_09_01,"2019-11-03",2016).
:- halt.
% Text
% Alice has a son, Bob. From September 1st, 2015 to November 3rd, 2019, Alice and Bob lived in the same home. Bob married Charlie on October 23rd, 2018. Bob and Charlie filed a joint return for the year 2019.

% Question
% Section 152(c)(1)(E) applies to Bob for the year 2019. Contradiction

% Facts
person(alice_s152_c_1_E_neg).
person(bob_s152_c_1_E_neg).
person(charlie_s152_c_1_E_neg).

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

son_(bob_is_son_s152_c_1_E_neg).
agent_(bob_is_son_s152_c_1_E_neg,bob_s152_c_1_E_neg).
patient_(bob_is_son_s152_c_1_E_neg,alice_s152_c_1_E_neg).
residence_(alice_and_bob_s152_c_1_E_neg).
agent_(alice_and_bob_s152_c_1_E_neg,alice_s152_c_1_E_neg).
agent_(alice_and_bob_s152_c_1_E_neg,bob_s152_c_1_E_neg).
patient_(alice_and_bob_s152_c_1_E_neg,home_s152_c_1_E_neg).
start_(alice_and_bob_s152_c_1_E_neg,d2015_09_01).
end_(alice_and_bob_s152_c_1_E_neg,d2019_11_03).
marriage_(bob_and_charlie_s152_c_1_E_neg).
agent_(bob_and_charlie_s152_c_1_E_neg,bob_s152_c_1_E_neg).
agent_(bob_and_charlie_s152_c_1_E_neg,charlie_s152_c_1_E_neg).
start_(bob_and_charlie_s152_c_1_E_neg,d2018_10_23).
joint_return_(bob_and_charlie_joint_return_s152_c_1_E_neg).
agent_(bob_and_charlie_joint_return_s152_c_1_E_neg,bob_s152_c_1_E_neg).
agent_(bob_and_charlie_joint_return_s152_c_1_E_neg,charlie_s152_c_1_E_neg).
start_(bob_and_charlie_joint_return_s152_c_1_E_neg,d2019_01_01).
end_(bob_and_charlie_joint_return_s152_c_1_E_neg,d2019_12_31).

% Test
:- \+ s152_c_1_E(bob_s152_c_1_E_neg,charlie_s152_c_1_E_neg,2019).
:- halt.
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
:- halt.
% Text
% Alice has a son, Bob. From September 1st, 2015 to February 3rd, 2019, Alice and Bob lived in the same home. Bob married Charlie on October 23rd, 2018. Bob bears a relationship to Alice pursuant to section 152(c)(2) for the years 2015 to 2020.

% Question
% Under section 152(c)(1), Bob is a qualifying child of Alice for the year 2019. Contradiction

% Facts
person(alice_s152_c_1_neg).
person(bob_s152_c_1_neg).
person(charlie_s152_c_1_neg).

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
date(d2019_02_03).
date_split(d2019_02_03, 2019, 2, 3).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

year(2020).
date_split(d2020_01_01, 2020, 1, 1).
date(d2020_12_31).
date_split(d2020_12_31, 2020, 12, 31).

son_(bob_is_son_s152_c_1_neg).
agent_(bob_is_son_s152_c_1_neg,bob_s152_c_1_neg).
patient_(bob_is_son_s152_c_1_neg,alice_s152_c_1_neg).
residence_(alice_and_bob_s152_c_1_neg).
agent_(alice_and_bob_s152_c_1_neg,alice_s152_c_1_neg).
agent_(alice_and_bob_s152_c_1_neg,bob_s152_c_1_neg).
patient_(alice_and_bob_s152_c_1_neg,home_s152_c_1_neg).
start_(alice_and_bob_s152_c_1_neg,d2015_09_01).
end_(alice_and_bob_s152_c_1_neg,d2019_02_03).
marriage_(bob_and_charlie_s152_c_1_neg).
agent_(bob_and_charlie_s152_c_1_neg,bob_s152_c_1_neg).
agent_(bob_and_charlie_s152_c_1_neg,charlie_s152_c_1_neg).
start_(bob_and_charlie_s152_c_1_neg,d2018_10_23).
s152_c_2(bob_s152_c_1_neg,alice_s152_c_1_neg,d2015_01_01,"2020-12-31").

% Test
:- \+ s152_c_1(bob_s152_c_1_neg,alice_s152_c_1_neg,2019).
:- halt.
% Text
% Alice has a son, Bob. From September 1st, 2015 to November 3rd, 2019, Alice and Bob lived in the same home. Bob married Charlie on October 23rd, 2018. Bob satisfied section 152(c)(2) and 152(c)(3) with Alice as the taxpayer for the years 2015 to 2020.

% Question
% Under section 152(c)(1), Bob is a qualifying child of Alice for the year 2019. Entailment

% Facts
person(alice_s152_c_1_pos).
person(bob_s152_c_1_pos).
person(charlie_s152_c_1_pos).

year(2015).
date(d2015_09_01).
date_split(d2015_09_01, 2015, 9, 1).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

year(2016).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

year(2017).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

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

year(2020).
date_split(d2020_01_01, 2020, 1, 1).
date(d2020_12_31).
date_split(d2020_12_31, 2020, 12, 31).

son_(bob_is_son_s152_c_1_pos).
agent_(bob_is_son_s152_c_1_pos,bob_s152_c_1_pos).
patient_(bob_is_son_s152_c_1_pos,alice_s152_c_1_pos).
residence_(alice_and_bob_s152_c_1_pos).
agent_(alice_and_bob_s152_c_1_pos,alice_s152_c_1_pos).
agent_(alice_and_bob_s152_c_1_pos,bob_s152_c_1_pos).
patient_(alice_and_bob_s152_c_1_pos,home_s152_c_1_pos).
start_(alice_and_bob_s152_c_1_pos,d2015_09_01).
end_(alice_and_bob_s152_c_1_pos,d2019_11_03).
marriage_(bob_and_charlie_s152_c_1_pos).
agent_(bob_and_charlie_s152_c_1_pos,bob_s152_c_1_pos).
agent_(bob_and_charlie_s152_c_1_pos,charlie_s152_c_1_pos).
start_(bob_and_charlie_s152_c_1_pos,d2018_10_23).
s152_c_2(bob_s152_c_1_pos,alice_s152_c_1_pos,d2015_01_01,"2020-12-31").
s152_c_3(bob_s152_c_1_pos,alice_s152_c_1_pos,Year) :- between(2015,2020,Year).

% Test
:- s152_c_1(bob_s152_c_1_pos,alice_s152_c_1_pos,2019).
:- halt.
% Text
% Alice has a son, Bob, who was born January 31st, 2014.

% Question
% Bob bears a relationship to Alice under section 152(c)(2)(B). Contradiction

% Facts
person(alice_s152_c_2_B_neg).
person(bob_s152_c_2_B_neg).

year(2014).
date(d2014_01_31).
date_split(d2014_01_31, 2014, 1, 31).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).
date(d2100_01_01).
date_split(d2100_01_01, 2100, 1, 1).

son_(alice_and_bob_s152_c_2_B_neg).
agent_(alice_and_bob_s152_c_2_B_neg,bob_s152_c_2_B_neg).
patient_(alice_and_bob_s152_c_2_B_neg,alice_s152_c_2_B_neg).
start_(alice_and_bob_s152_c_2_B_neg,d2014_01_31).

% Test
:- \+ s152_c_2_B(bob_s152_c_2_B_neg,alice_s152_c_2_B_neg,bob_s152_c_2_B_neg,d2014_01_31,"2100-01-01").
:- halt.
% Text
% Alice has a brother, Bob, who was born January 31st, 2014.

% Question
% Bob bears a relationship to Alice under section 152(c)(2)(B). Entailment

% Facts
person(alice_s152_c_2_B_pos).
person(bob_s152_c_2_B_pos).

year(2014).
date(d2014_01_31).
date_split(d2014_01_31, 2014, 1, 31).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).
date(d2100_01_01).
date_split(d2100_01_01, 2100, 1, 1).

brother_(alice_and_bob_s152_c_2_B_pos).
agent_(alice_and_bob_s152_c_2_B_pos,bob_s152_c_2_B_pos).
patient_(alice_and_bob_s152_c_2_B_pos,alice_s152_c_2_B_pos).
start_(alice_and_bob_s152_c_2_B_pos,d2014_01_31).

% Test
:- s152_c_2_B(bob_s152_c_2_B_pos,alice_s152_c_2_B_pos,bob_s152_c_2_B_pos,d2014_01_31,"2100-01-01").
:- halt.
% Text
% Alice has a son, Bob, who was born January 31st, 2014.

% Question
% Alice bears a relationship to Bob under section 152(c)(2). Contradiction

% Facts
person(alice_s152_c_2_neg).
person(bob_s152_c_2_neg).

year(2014).
date(d2014_01_31).
date_split(d2014_01_31, 2014, 1, 31).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).
date(d2100_01_01).
date_split(d2100_01_01, 2100, 1, 1).

son_(alice_and_bob_s152_c_2_neg).
agent_(alice_and_bob_s152_c_2_neg,bob_s152_c_2_neg).
patient_(alice_and_bob_s152_c_2_neg,alice_s152_c_2_neg).
start_(alice_and_bob_s152_c_2_neg,d2014_01_31).

% Test
:- \+ s152_c_2(alice_s152_c_2_neg,bob_s152_c_2_neg,d2014_01_31,"2100-01-01").
:- halt.
% Text
% Alice has a son, Bob, who was born January 31st, 2014.

% Question
% Bob bears a relationship to Alice under section 152(c)(2). Entailment

% Facts
person(alice_s152_c_2_pos).
person(bob_s152_c_2_pos).

year(2014).
date(d2014_01_31).
date_split(d2014_01_31, 2014, 1, 31).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).
date(d2100_01_01).
date_split(d2100_01_01, 2100, 1, 1).

son_(alice_and_bob_s152_c_2_pos).
agent_(alice_and_bob_s152_c_2_pos,bob_s152_c_2_pos).
patient_(alice_and_bob_s152_c_2_pos,alice_s152_c_2_pos).
start_(alice_and_bob_s152_c_2_pos,d2014_01_31).

% Test
:- s152_c_2(bob_s152_c_2_pos,alice_s152_c_2_pos,d2014_01_31,"2100-01-01").
:- halt.
% Text
% Alice was born January 10th, 1992. Bob was born January 31st, 1984. Alice adopted Bob on March 4th, 2018.

% Question
% Bob satisfies section 152(c)(3) with Alice claiming Bob as a qualifying child for the year 2019. Contradiction

% Facts
person(alice_s152_c_3_neg).
person(bob_s152_c_3_neg).

year(1992).
date(d1992_01_10).
date_split(d1992_01_10, 1992, 1, 10).
date(d1992_01_01).
date_split(d1992_01_01, 1992, 1, 1).
date(d1992_12_31).
date_split(d1992_12_31, 1992, 12, 31).

year(1984).
date(d1984_01_31).
date_split(d1984_01_31, 1984, 1, 31).
date(d1984_01_01).
date_split(d1984_01_01, 1984, 1, 1).
date(d1984_12_31).
date_split(d1984_12_31, 1984, 12, 31).

year(2018).
date(d2018_03_04).
date_split(d2018_03_04, 2018, 3, 4).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

birth_(alice_is_born_s152_c_3_neg).
agent_(alice_is_born_s152_c_3_neg,alice_s152_c_3_neg).
start_(alice_is_born_s152_c_3_neg,d1992_01_10).
end_(alice_is_born_s152_c_3_neg,d1992_01_10).
birth_(bob_is_born_s152_c_3_neg).
agent_(bob_is_born_s152_c_3_neg,bob_s152_c_3_neg).
start_(bob_is_born_s152_c_3_neg,d1984_01_31).
end_(bob_is_born_s152_c_3_neg,d1984_01_31).
son_(alice_and_bob_s152_c_3_neg).
agent_(alice_and_bob_s152_c_3_neg,bob_s152_c_3_neg).
patient_(alice_and_bob_s152_c_3_neg,alice_s152_c_3_neg).
start_(alice_and_bob_s152_c_3_neg,d2018_03_04).

% Test
:- \+ s152_c_3(bob_s152_c_3_neg,alice_s152_c_3_neg,2019).
:- halt.
% Text
% Alice was born January 10th, 1992. Bob was born January 31st, 2014. Alice adopted Bob on March 4th, 2018.

% Question
% Bob satisfies section 152(c)(3) with Alice claiming Bob as a qualifying child for the year 2019. Entailment

% Facts
person(alice_s152_c_3_pos).
person(bob_s152_c_3_pos).

year(1992).
date(d1992_01_10).
date_split(d1992_01_10, 1992, 1, 10).
date(d1992_01_01).
date_split(d1992_01_01, 1992, 1, 1).
date(d1992_12_31).
date_split(d1992_12_31, 1992, 12, 31).

year(2014).
date(d2014_01_31).
date_split(d2014_01_31, 2014, 1, 31).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).

year(2018).
date(d2018_03_04).
date_split(d2018_03_04, 2018, 3, 4).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

birth_(alice_is_born_s152_c_3_pos).
agent_(alice_is_born_s152_c_3_pos,alice_s152_c_3_pos).
start_(alice_is_born_s152_c_3_pos,d1992_01_10).
end_(alice_is_born_s152_c_3_pos,d1992_01_10).
birth_(bob_is_born_s152_c_3_pos).
agent_(bob_is_born_s152_c_3_pos,bob_s152_c_3_pos).
start_(bob_is_born_s152_c_3_pos,d2014_01_31).
end_(bob_is_born_s152_c_3_pos,d2014_01_31).
son_(alice_and_bob_s152_c_3_pos).
agent_(alice_and_bob_s152_c_3_pos,bob_s152_c_3_pos).
patient_(alice_and_bob_s152_c_3_pos,alice_s152_c_3_pos).
start_(alice_and_bob_s152_c_3_pos,d2018_03_04).

% Test
:- s152_c_3(bob_s152_c_3_pos,alice_s152_c_3_pos,2019).
:- halt.
% Text
% In 2015, Alice's income was $2312. The exemption amount for Alice under section 151(d) for the year 2015 was $2000.

% Question
% Section 152(d)(1)(B) applies to Alice for the year 2015. Contradiction

% Facts
person(alice_s152_d_1_B_neg).

finance(2312).
finance(2000).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

income_(alice_makes_money_s152_d_1_B_neg).
agent_(alice_makes_money_s152_d_1_B_neg,alice_s152_d_1_B_neg).
amount_(alice_makes_money_s152_d_1_B_neg,2312).
start_(alice_makes_money_s152_d_1_B_neg,d2015_01_01).
end_(alice_makes_money_s152_d_1_B_neg,d2015_12_31).
s151_d(alice_s152_d_1_B_neg,2000,2015).

% Test
:- \+ s152_d_1_B(alice_s152_d_1_B_neg,2015).
:- halt.
% Text
% In 2015, Alice did not have any income. The exemption amount for Alice under section 151(d) for the year 2015 was $2000.

% Question
% Section 152(d)(1)(B) applies to Alice for the year 2015. Entailment

% Facts
person(alice_s152_d_1_B_pos).

finance(2000).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

s151_d(alice_s152_d_1_B_pos,2000,2015).

% Test
:- s152_d_1_B(alice_s152_d_1_B_pos,2015).
:- halt.
% Text
% Bob is Alice's son since April 15th, 2014.

% Question
% Alice bears a relationship to Bob under section 152(d)(2)(B) for the year 2015. Contradiction

% Facts
person(alice_s152_d_2_B_neg).
person(bob_s152_d_2_B_neg).

year(2014).
date(d2014_04_15).
date_split(d2014_04_15, 2014, 4, 15).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).
date(d2100_01_01).
date_split(d2100_01_01, 2100, 1, 1).

son_(alice_and_bob_s152_d_2_B_neg).
agent_(alice_and_bob_s152_d_2_B_neg,bob_s152_d_2_B_neg).
patient_(alice_and_bob_s152_d_2_B_neg,alice_s152_d_2_B_neg).
start_(alice_and_bob_s152_d_2_B_neg,d2014_04_15).

% Test
:- \+ s152_d_2_B(alice_s152_d_2_B_neg,bob_s152_d_2_B_neg,d2014_04_15,"2100-01-01").
:- halt.
% Text
% Bob is Alice's brother since April 15th, 2014.

% Question
% Alice bears a relationship to Bob under section 152(d)(2)(B) for the year 2015. Entailment

% Facts
person(alice_s152_d_2_B_pos).
person(bob_s152_d_2_B_pos).

year(2014).
date(d2014_04_15).
date_split(d2014_04_15, 2014, 4, 15).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).
date(d2100_01_01).
date_split(d2100_01_01, 2100, 1, 1).

brother_(alice_and_bob_s152_d_2_B_pos).
agent_(alice_and_bob_s152_d_2_B_pos,bob_s152_d_2_B_pos).
patient_(alice_and_bob_s152_d_2_B_pos,alice_s152_d_2_B_pos).
start_(alice_and_bob_s152_d_2_B_pos,d2014_04_15).

% Test
:- s152_d_2_B(alice_s152_d_2_B_pos,bob_s152_d_2_B_pos,d2014_04_15,"2100-01-01").
:- halt.
% Text
% Charlie is Alice's father since April 15th, 2014. Bob is Charlie's brother since October 12th, 1992.

% Question
% Alice bears a relationship to Bob under section 152(d)(2)(D) for the year 2018. Contradiction

% Facts
person(alice_s152_d_2_D_neg).
person(bob_s152_d_2_D_neg).
person(charlie_s152_d_2_D_neg).

year(1992).
date(d1992_10_12).
date_split(d1992_10_12, 1992, 10, 12).
date(d1992_01_01).
date_split(d1992_01_01, 1992, 1, 1).
date(d1992_12_31).
date_split(d1992_12_31, 1992, 12, 31).

year(2014).
date(d2014_04_15).
date_split(d2014_04_15, 2014, 4, 15).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).

year(2018).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).
date(d2100_01_01).
date_split(d2100_01_01, 2100, 1, 1).

father_(alice_and_bob_s152_d_2_D_neg).
agent_(alice_and_bob_s152_d_2_D_neg,bob_s152_d_2_D_neg).
patient_(alice_and_bob_s152_d_2_D_neg,alice_s152_d_2_D_neg).
start_(alice_and_bob_s152_d_2_D_neg,d2014_04_15).
brother_(bob_and_charlie_s152_d_2_D_neg).
agent_(bob_and_charlie_s152_d_2_D_neg,bob_s152_d_2_D_neg).
patient_(bob_and_charlie_s152_d_2_D_neg,charlie_s152_d_2_D_neg).
start_(bob_and_charlie_s152_d_2_D_neg,d1992_10_12).
% neg_s152_d_2_D():-
%     s152_d_2_D(alice,bob,Start_relationship,End_relationship),
%     first_day_year(2018,First_day),
%     is_before(Start_relationship,First_day).

% Test
:- \+ s152_d_2_D(alice_s152_d_2_D_neg,bob_s152_d_2_D_neg,d2014_04_15,"2100-01-01").
:- halt.
% Text
% Charlie is Bob's father since April 15th, 1995. Dorothy is Bob's mother. Alice married Charlie on August 8th, 2018.

% Question
% Alice bears a relationship to Bob under section 152(d)(2)(D) for the year 2019. Entailment

% Facts
person(alice_s152_d_2_D_pos).
person(bob_s152_d_2_D_pos).
person(charlie_s152_d_2_D_pos).
person(dorothy_s152_d_2_D_pos).

year(1995).
date(d1995_04_15).
date_split(d1995_04_15, 1995, 4, 15).
date(d1995_01_01).
date_split(d1995_01_01, 1995, 1, 1).
date(d1995_12_31).
date_split(d1995_12_31, 1995, 12, 31).

year(2018).
date(d2018_08_08).
date_split(d2018_08_08, 2018, 8, 8).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).
date(d2100_01_01).
date_split(d2100_01_01, 2100, 1, 1).

father_(charlie_and_bob_s152_d_2_D_pos).
agent_(charlie_and_bob_s152_d_2_D_pos,charlie_s152_d_2_D_pos).
patient_(charlie_and_bob_s152_d_2_D_pos,bob_s152_d_2_D_pos).
start_(charlie_and_bob_s152_d_2_D_pos,d1995_04_15).
mother_(dorothy_and_bob_s152_d_2_D_pos).
agent_(dorothy_and_bob_s152_d_2_D_pos,dorothy_s152_d_2_D_pos).
patient_(dorothy_and_bob_s152_d_2_D_pos,bob_s152_d_2_D_pos).
start_(dorothy_and_bob_s152_d_2_D_pos,d1995_04_15).
marriage_(alice_and_charlie_s152_d_2_D_pos).
agent_(alice_and_charlie_s152_d_2_D_pos,alice_s152_d_2_D_pos).
agent_(alice_and_charlie_s152_d_2_D_pos,charlie_s152_d_2_D_pos).
start_(alice_and_charlie_s152_d_2_D_pos,d2018_08_08).
% pos_s152_d_2_D():-
%     s152_d_2_D(alice,bob,Start_relationship,End_relationship),
%     first_day_year(2019,First_day),
%     is_before(Start_relationship,First_day).

% Test
:- s152_d_2_D(alice_s152_d_2_D_pos,bob_s152_d_2_D_pos,d2018_08_08,"2100-01-01").
:- halt.
% Text
% Charlie is Bob's father since April 15th, 2014. Alice is Charlie's sister since October 12th, 1992.

% Question
% Alice bears a relationship to Bob under section 152(d)(2)(E). Contradiction

% Facts
person(alice_s152_d_2_E_neg).
person(bob_s152_d_2_E_neg).
person(charlie_s152_d_2_E_neg).

year(2014).
date(d2014_04_15).
date_split(d2014_04_15, 2014, 4, 15).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).

year(1992).
date(d1992_10_12).
date_split(d1992_10_12, 1992, 10, 12).
date(d1992_01_01).
date_split(d1992_01_01, 1992, 1, 1).
date(d1992_12_31).
date_split(d1992_12_31, 1992, 12, 31).

year(2100).
date(d2100_01_01).
date_split(d2100_01_01, 2100, 1, 1).

father_(charlie_and_bob_s152_d_2_E_neg).
agent_(charlie_and_bob_s152_d_2_E_neg,charlie_s152_d_2_E_neg).
patient_(charlie_and_bob_s152_d_2_E_neg,bob_s152_d_2_E_neg).
start_(charlie_and_bob_s152_d_2_E_neg,d2014_04_15).
sister_(alice_and_charlie_s152_d_2_E_neg).
agent_(alice_and_charlie_s152_d_2_E_neg,alice_s152_d_2_E_neg).
patient_(alice_and_charlie_s152_d_2_E_neg,charlie_s152_d_2_E_neg).
start_(alice_and_charlie_s152_d_2_E_neg,d1992_10_12).

% Test
:- \+ s152_d_2_E(alice_s152_d_2_E_neg,bob_s152_d_2_E_neg,charlie_s152_d_2_E_neg,d2014_04_15,"2100-01-01").
:- halt.
% Text
% Charlie is Alice's father since April 15th, 2014. Bob is Charlie's brother since October 12th, 1992.

% Question
% Alice bears a relationship to Bob under section 152(d)(2)(E). Entailment

% Facts
person(alice_s152_d_2_E_pos).
person(bob_s152_d_2_E_pos).
person(charlie_s152_d_2_E_pos).

year(2014).
date(d2014_04_15).
date_split(d2014_04_15, 2014, 4, 15).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).

year(1992).
date(d1992_10_12).
date_split(d1992_10_12, 1992, 10, 12).
date(d1992_01_01).
date_split(d1992_01_01, 1992, 1, 1).
date(d1992_12_31).
date_split(d1992_12_31, 1992, 12, 31).

father_(alice_and_charlie_s152_d_2_E_pos).
agent_(alice_and_charlie_s152_d_2_E_pos,charlie_s152_d_2_E_pos).
patient_(alice_and_charlie_s152_d_2_E_pos,alice_s152_d_2_E_pos).
start_(alice_and_charlie_s152_d_2_E_pos,d2014_04_15).
brother_(bob_and_charlie_s152_d_2_E_pos).
agent_(bob_and_charlie_s152_d_2_E_pos,bob_s152_d_2_E_pos).
patient_(bob_and_charlie_s152_d_2_E_pos,charlie_s152_d_2_E_pos).
start_(bob_and_charlie_s152_d_2_E_pos,d1992_10_12).

% Test
:- s152_d_2_E(alice_s152_d_2_E_pos,bob_s152_d_2_E_pos,charlie_s152_d_2_E_pos,d2014_04_15,"2100-01-01").
:- halt.
% Text
% Charlie is Bob's father since April 15th, 2014. Alice married Charlie on October 12th, 1992.

% Question
% Alice bears a relationship to Bob under section 152(d)(2)(F). Contradiction

% Facts
person(alice_s152_d_2_F_neg).
person(bob_s152_d_2_F_neg).
person(charlie_s152_d_2_F_neg).

year(2014).
date(d2014_04_15).
date_split(d2014_04_15, 2014, 4, 15).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).

year(1992).
date(d1992_10_12).
date_split(d1992_10_12, 1992, 10, 12).
date(d1992_01_01).
date_split(d1992_01_01, 1992, 1, 1).
date(d1992_12_31).
date_split(d1992_12_31, 1992, 12, 31).

year(2100).
date(d2100_01_01).
date_split(d2100_01_01, 2100, 1, 1).

father_(charlie_and_bob_s152_d_2_F_neg).
agent_(charlie_and_bob_s152_d_2_F_neg,charlie_s152_d_2_F_neg).
patient_(charlie_and_bob_s152_d_2_F_neg,bob_s152_d_2_F_neg).
start_(charlie_and_bob_s152_d_2_F_neg,d2014_04_15).
marriage_(alice_and_charlie_s152_d_2_F_neg).
agent_(alice_and_charlie_s152_d_2_F_neg,alice_s152_d_2_F_neg).
agent_(alice_and_charlie_s152_d_2_F_neg,charlie_s152_d_2_F_neg).
start_(alice_and_charlie_s152_d_2_F_neg,d1992_10_12).

% Test
:- \+ s152_d_2_F(alice_s152_d_2_F_neg,bob_s152_d_2_F_neg,charlie_s152_d_2_F_neg,d2014_04_15,"2100-01-01").
:- halt.
% Text
% Charlie is Bob's father since April 15th, 2014. Alice is Charlie's sister since October 12th, 1992.

% Question
% Alice bears a relationship to Bob under section 152(d)(2)(F). Entailment

% Facts
person(alice_s152_d_2_F_pos).
person(bob_s152_d_2_F_pos).
person(charlie_s152_d_2_F_pos).

year(2014).
date(d2014_04_15).
date_split(d2014_04_15, 2014, 4, 15).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).

year(1992).
date(d1992_10_12).
date_split(d1992_10_12, 1992, 10, 12).
date(d1992_01_01).
date_split(d1992_01_01, 1992, 1, 1).
date(d1992_12_31).
date_split(d1992_12_31, 1992, 12, 31).

year(2100).
date(d2100_01_01).
date_split(d2100_01_01, 2100, 1, 1).

father_(charlie_and_bob_s152_d_2_F_pos).
agent_(charlie_and_bob_s152_d_2_F_pos,charlie_s152_d_2_F_pos).
patient_(charlie_and_bob_s152_d_2_F_pos,bob_s152_d_2_F_pos).
start_(charlie_and_bob_s152_d_2_F_pos,d2014_04_15).
sister_(alice_and_charlie_s152_d_2_F_pos).
agent_(alice_and_charlie_s152_d_2_F_pos,alice_s152_d_2_F_pos).
patient_(alice_and_charlie_s152_d_2_F_pos,charlie_s152_d_2_F_pos).
start_(alice_and_charlie_s152_d_2_F_pos,d1992_10_12).

% Test
:- s152_d_2_F(alice_s152_d_2_F_pos,bob_s152_d_2_F_pos,charlie_s152_d_2_F_pos,d2014_04_15,"2100-01-01").
:- halt.
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
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice died on July 9th, 2014.

% Question
% Section 2(a)(1)(A) applies to Bob in 2014. Contradiction

% Facts
person(alice_s2_a_1_A_neg).
person(bob_s2_a_1_A_neg).
year(2014).
year(1992).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).
date(d2014_07_09).
date_split(d2014_07_09,2014,7,9).
date(d2014_01_01).
date_split(d2014_01_01,2014,1,1).
date(d2014_12_31).
date_split(d2014_12_31,2014,12,31).

marriage_(alice_and_bob_s2_a_1_A_neg).
agent_(alice_and_bob_s2_a_1_A_neg,alice_s2_a_1_A_neg).
agent_(alice_and_bob_s2_a_1_A_neg,bob_s2_a_1_A_neg).
start_(alice_and_bob_s2_a_1_A_neg,d1992_02_03).
death_(alice_dies_s2_a_1_A_neg).
agent_(alice_dies_s2_a_1_A_neg,alice_s2_a_1_A_neg).
start_(alice_dies_s2_a_1_A_neg,d2014_07_09).

% Test
:- \+ s2_a_1_A(bob_s2_a_1_A_neg,alice_s2_a_1_A_neg,alice_and_bob_s2_a_1_A_neg,2014,2014).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice died on July 9th, 2014.

% Question
% Section 2(a)(1)(A) applies to Bob in 2015. Entailment

% Facts
person(alice_s2_a_1_A_pos).
person(bob_s2_a_1_A_pos).
year(2014).
year(1992).
year(2015).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).
date(d2014_07_09).
date_split(d2014_07_09,2014,7,9).
date(d2014_01_01).
date_split(d2014_01_01,2014,1,1).
date(d2014_12_31).
date_split(d2014_12_31,2014,12,31).
marriage_(alice_and_bob_s2_a_1_A_pos).
agent_(alice_and_bob_s2_a_1_A_pos,alice_s2_a_1_A_pos).
agent_(alice_and_bob_s2_a_1_A_pos,bob_s2_a_1_A_pos).
start_(alice_and_bob_s2_a_1_A_pos,d1992_02_03).
death_(alice_dies_s2_a_1_A_pos).
agent_(alice_dies_s2_a_1_A_pos,alice_s2_a_1_A_pos).
start_(alice_dies_s2_a_1_A_pos,d2014_07_09).

% Test
:- s2_a_1_A(bob_s2_a_1_A_pos,alice_s2_a_1_A_pos,alice_and_bob_s2_a_1_A_pos,2014,2015).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice died on July 9th, 2014. Bob married Charlie on September 14th, 2015.

% Question
% Section 2(a)(2)(A) applies to Bob in 2014. Contradiction

% Facts
person(alice_s2_a_2_A_neg).
person(bob_s2_a_2_A_neg).
person(charlie_s2_a_2_A_neg).

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

marriage_(alice_and_bob_s2_a_2_A_neg).
agent_(alice_and_bob_s2_a_2_A_neg,alice_s2_a_2_A_neg).
agent_(alice_and_bob_s2_a_2_A_neg,bob_s2_a_2_A_neg).
start_(alice_and_bob_s2_a_2_A_neg,d1992_02_03).
death_(alice_dies_s2_a_2_A_neg).
agent_(alice_dies_s2_a_2_A_neg,alice_s2_a_2_A_neg).
start_(alice_dies_s2_a_2_A_neg,d2014_07_09).
end_(alice_dies_s2_a_2_A_neg,d2014_07_09).
marriage_(alice_and_charlie_s2_a_2_A_neg).
agent_(alice_and_charlie_s2_a_2_A_neg,charlie_s2_a_2_A_neg).
agent_(alice_and_charlie_s2_a_2_A_neg,bob_s2_a_2_A_neg).
start_(alice_and_charlie_s2_a_2_A_neg,d2015_09_14).

% Test
:- \+ s2_a_2_A(bob_s2_a_2_A_neg,alice_and_charlie_s2_a_2_A_neg,alice_and_bob_s2_a_2_A_neg,d2015_09_14,2014).
:- halt.
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
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice died on July 9th, 2014. Alice was a nonresident alien since March 4th, 1990.

% Question
% Section 2(a)(2)(B) applies to Bob in 2014. Contradiction

% Facts
person(alice_s2_a_2_B_neg).
person(bob_s2_a_2_B_neg).

year(1990).
date(d1990_03_04).
date_split(d1990_03_04,1990,3,4).
date(d1990_01_01).
date_split(d1990_01_01,1990,1,1).
date(d1990_12_31).
date_split(d1990_12_31,1990,12,31).

year(1992).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).

marriage_(alice_and_bob_s2_a_2_B_neg).
agent_(alice_and_bob_s2_a_2_B_neg,alice_s2_a_2_B_neg).
agent_(alice_and_bob_s2_a_2_B_neg,bob_s2_a_2_B_neg).
start_(alice_and_bob_s2_a_2_B_neg,d1992_02_03).
death_(alice_dies_s2_a_2_B_neg).
agent_(alice_dies_s2_a_2_B_neg,alice_s2_a_2_B_neg).
start_(alice_dies_s2_a_2_B_neg,d2014_07_09).
end_(alice_dies_s2_a_2_B_neg,d2014_07_09).
nonresident_alien_(alice_is_nra_s2_a_2_B_neg).
agent_(alice_is_nra_s2_a_2_B_neg,alice_s2_a_2_B_neg).
start_(alice_is_nra_s2_a_2_B_neg,d1990_03_04).

% Test
:- \+ s2_a_2_B(bob_s2_a_2_B_neg,alice_s2_a_2_B_neg,2014).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice died on July 9th, 2014.

% Question
% Section 2(a)(2)(B) applies to Bob in 2014. Entailment

% Facts
person(alice_s2_a_2_B_pos).
person(bob_s2_a_2_B_pos).

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

marriage_(alice_and_bob_s2_a_2_B_pos).
agent_(alice_and_bob_s2_a_2_B_pos,alice_s2_a_2_B_pos).
agent_(alice_and_bob_s2_a_2_B_pos,bob_s2_a_2_B_pos).
start_(alice_and_bob_s2_a_2_B_pos,d1992_02_03).
death_(alice_dies_s2_a_2_B_pos).
agent_(alice_dies_s2_a_2_B_pos,alice_s2_a_2_B_pos).
start_(alice_dies_s2_a_2_B_pos,d2014_07_09).
end_(alice_dies_s2_a_2_B_pos,d2014_07_09).

% Test
:- s2_a_2_B(bob_s2_a_2_B_pos,alice_s2_a_2_B_pos,2014).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice and Bob have a child, Charlie, born October 9th, 2000. Alice died on July 9th, 2014. From 2004 to 2019, Bob furnished 40% of the costs of maintaining the home where he and Charlie lived during that time. Charlie is not the dependent of Bob under section 152(b)(2).

% Question
% Section 2(b)(1)(A) applies to Bob in 2018. Contradiction

% Facts
person(alice_s2_b_1_A_neg).
person(bob_s2_b_1_A_neg).
person(charlie_s2_b_1_A_neg).
person(someone).

year(1992).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).

year(2000).
date(d2000_10_09).
date_split(d2000_10_09,2000,10,9).
date(d2000_01_01).
date_split(d2000_01_01,2000,1,1).
date(d2000_12_31).
date_split(d2000_12_31,2000,12,31).

year(2004).
date(d2004_01_01).
date_split(d2004_01_01,2004,1,1).
date(d2004_12_31).
date_split(d2004_12_31,2004,12,31).

year(2005).
date(d2005_01_01).
date_split(d2005_01_01,2005,1,1).
date(d2005_12_31).
date_split(d2005_12_31,2005,12,31).

year(2006).
date(d2006_01_01).
date_split(d2006_01_01,2006,1,1).
date(d2006_12_31).
date_split(d2006_12_31,2006,12,31).

year(2007).
date(d2007_01_01).
date_split(d2007_01_01,2007,1,1).
date(d2007_12_31).
date_split(d2007_12_31,2007,12,31).

year(2008).
date(d2008_01_01).
date_split(d2008_01_01,2008,1,1).
date(d2008_12_31).
date_split(d2008_12_31,2008,12,31).

year(2009).
date(d2009_01_01).
date_split(d2009_01_01,2009,1,1).
date(d2009_12_31).
date_split(d2009_12_31,2009,12,31).

year(2010).
date(d2010_01_01).
date_split(d2010_01_01,2010,1,1).
date(d2010_12_31).
date_split(d2010_12_31,2010,12,31).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01,2011,1,1).
date(d2011_12_31).
date_split(d2011_12_31,2011,12,31).

year(2012).
date(d2012_01_01).
date_split(d2012_01_01,2012,1,1).
date(d2012_12_31).
date_split(d2012_12_31,2012,12,31).

year(2013).
date(d2013_01_01).
date_split(d2013_01_01,2013,1,1).
date(d2013_12_31).
date_split(d2013_12_31,2013,12,31).

year(2014).
date(d2014_07_09).
date_split(d2014_07_09,2014,7,9).
date(d2014_01_01).
date_split(d2014_01_01,2014,1,1).
date(d2014_12_31).
date_split(d2014_12_31,2014,12,31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01,2015,1,1).
date(d2015_12_31).
date_split(d2015_12_31,2015,12,31).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01,2016,1,1).
date(d2016_12_31).
date_split(d2016_12_31,2016,12,31).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

year(2018).
date(d2018_02_14).
date_split(d2018_02_14,2018,2,14).
date(d2018_01_01).
date_split(d2018_01_01,2018,1,1).
date(d2018_12_31).
date_split(d2018_12_31,2018,12,31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01,2019,1,1).
date(d2019_12_31).
date_split(d2019_12_31,2019,12,31).

atom_concat('bob_maintains_household_s2_b_1_A_neg',2004,bob_maintains_household_s2_b_1_A_neg2004).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2005,bob_maintains_household_s2_b_1_A_neg2005).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2006,bob_maintains_household_s2_b_1_A_neg2006).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2007,bob_maintains_household_s2_b_1_A_neg2007).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2008,bob_maintains_household_s2_b_1_A_neg2008).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2009,bob_maintains_household_s2_b_1_A_neg2009).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2010,bob_maintains_household_s2_b_1_A_neg2010).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2011,bob_maintains_household_s2_b_1_A_neg2011).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2012,bob_maintains_household_s2_b_1_A_neg2012).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2013,bob_maintains_household_s2_b_1_A_neg2013).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2014,bob_maintains_household_s2_b_1_A_neg2014).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2015,bob_maintains_household_s2_b_1_A_neg2015).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2016,bob_maintains_household_s2_b_1_A_neg2016).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2017,bob_maintains_household_s2_b_1_A_neg2017).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2018,bob_maintains_household_s2_b_1_A_neg2018).
atom_concat('bob_maintains_household_s2_b_1_A_neg',2019,bob_maintains_household_s2_b_1_A_neg2019).

atom_concat('someone_maintains_household_s2_b_1_A_neg', 2004, someone_maintains_household_s2_b_1_A_neg2004).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2005, someone_maintains_household_s2_b_1_A_neg2005).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2006, someone_maintains_household_s2_b_1_A_neg2006).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2007, someone_maintains_household_s2_b_1_A_neg2007).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2008, someone_maintains_household_s2_b_1_A_neg2008).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2009, someone_maintains_household_s2_b_1_A_neg2009).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2010, someone_maintains_household_s2_b_1_A_neg2010).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2011, someone_maintains_household_s2_b_1_A_neg2011).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2012, someone_maintains_household_s2_b_1_A_neg2012).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2013, someone_maintains_household_s2_b_1_A_neg2013).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2014, someone_maintains_household_s2_b_1_A_neg2014).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2015, someone_maintains_household_s2_b_1_A_neg2015).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2016, someone_maintains_household_s2_b_1_A_neg2016).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2017, someone_maintains_household_s2_b_1_A_neg2017).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2018, someone_maintains_household_s2_b_1_A_neg2018).
atom_concat('someone_maintains_household_s2_b_1_A_neg', 2019, someone_maintains_household_s2_b_1_A_neg2019).

finance(40).
finance(60).

marriage_(alice_and_bob_s2_b_1_A_neg).
agent_(alice_and_bob_s2_b_1_A_neg,alice_s2_b_1_A_neg).
agent_(alice_and_bob_s2_b_1_A_neg,bob_s2_b_1_A_neg).
start_(alice_and_bob_s2_b_1_A_neg,d1992_02_03).
death_(alice_dies_s2_b_1_A_neg).
agent_(alice_dies_s2_b_1_A_neg,alice_s2_b_1_A_neg).
start_(alice_dies_s2_b_1_A_neg,d2014_07_09).
end_(alice_dies_s2_b_1_A_neg,d2014_07_09).
son_(charlie_is_son_s2_b_1_A_neg).
agent_(charlie_is_son_s2_b_1_A_neg,charlie_s2_b_1_A_neg).
patient_(charlie_is_son_s2_b_1_A_neg,alice_s2_b_1_A_neg).
patient_(charlie_is_son_s2_b_1_A_neg,bob_s2_b_1_A_neg).
start_(charlie_is_son_s2_b_1_A_neg,d2000_10_09).
residence_(charlie_and_bob_residence_s2_b_1_A_neg).
agent_(charlie_and_bob_residence_s2_b_1_A_neg,charlie_s2_b_1_A_neg).
agent_(charlie_and_bob_residence_s2_b_1_A_neg,bob_s2_b_1_A_neg).
patient_(charlie_and_bob_residence_s2_b_1_A_neg,bob_s_house_s2_b_1_A_neg).
start_(charlie_and_bob_residence_s2_b_1_A_neg,d2004_01_01).
end_(charlie_and_bob_residence_s2_b_1_A_neg,d2019_12_31).
bob_household_maintenance(Year,Event,Start_day,End_day) :-
    between(2004,2019,Year),
    atom_concat('bob_maintains_household_s2_b_1_A_neg',Year,Event),
    first_day_year(Year,Start_day),
    last_day_year(Year,End_day).
payment_(Event) :- bob_household_maintenance(_,Event,_,_).
agent_(Event,bob_s2_b_1_A_neg) :- bob_household_maintenance(_,Event,_,_).
amount_(Event,40) :- bob_household_maintenance(_,Event,_,_).
purpose_(Event,bob_s_house_s2_b_1_A_neg) :- bob_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- bob_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- bob_household_maintenance(_,Event,_,End_day).
someone_household_maintenance(Year,Event,Start_day,End_day) :-
    between(2004,2019,Year),
    atom_concat('someone_maintains_household_s2_b_1_A_neg',Year,Event),
    first_day_year(Year,Start_day),
    last_day_year(Year,End_day).
payment_(Event) :- someone_household_maintenance(_,Event,_,_).
agent_(Event,someone) :- someone_household_maintenance(_,Event,_,_).
amount_(Event,60) :- someone_household_maintenance(_,Event,_,_).
purpose_(Event,bob_s_house_s2_b_1_A_neg) :- someone_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- someone_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- someone_household_maintenance(_,Event,_,End_day).

% Test
:- \+ s2_b_1_A(bob_s2_b_1_A_neg,bob_s_house_s2_b_1_A_neg,charlie_s2_b_1_A_neg,2018).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice and Bob have a child, Charlie, born October 9th, 2000. Alice died on July 9th, 2014. From 2004 to 2019, Bob furnished the costs of maintaining the home where he and Charlie lived during that time. Charlie was a qualifying child of Bob under section 152(c) from 2004 to 2019.

% Question
% Section 2(b)(1)(A) applies to Bob in 2018. Entailment

% Facts
person(alice_s2_b_1_A_pos).
person(bob_s2_b_1_A_pos).
person(charlie_s2_b_1_A_pos).

year(1992).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).

year(2000).
date(d2000_10_09).
date_split(d2000_10_09,2000,10,9).
date(d2000_01_01).
date_split(d2000_01_01,2000,1,1).
date(d2000_12_31).
date_split(d2000_12_31,2000,12,31).

year(2004).
date(d2004_01_01).
date_split(d2004_01_01,2004,1,1).
date(d2004_12_31).
date_split(d2004_12_31,2004,12,31).

year(2005).
date(d2005_01_01).
date_split(d2005_01_01,2005,1,1).
date(d2005_12_31).
date_split(d2005_12_31,2005,12,31).

year(2006).
date(d2006_01_01).
date_split(d2006_01_01,2006,1,1).
date(d2006_12_31).
date_split(d2006_12_31,2006,12,31).

year(2007).
date(d2007_01_01).
date_split(d2007_01_01,2007,1,1).
date(d2007_12_31).
date_split(d2007_12_31,2007,12,31).

year(2008).
date(d2008_01_01).
date_split(d2008_01_01,2008,1,1).
date(d2008_12_31).
date_split(d2008_12_31,2008,12,31).

year(2009).
date(d2009_01_01).
date_split(d2009_01_01,2009,1,1).
date(d2009_12_31).
date_split(d2009_12_31,2009,12,31).

year(2010).
date(d2010_01_01).
date_split(d2010_01_01,2010,1,1).
date(d2010_12_31).
date_split(d2010_12_31,2010,12,31).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01,2011,1,1).
date(d2011_12_31).
date_split(d2011_12_31,2011,12,31).

year(2012).
date(d2012_01_01).
date_split(d2012_01_01,2012,1,1).
date(d2012_12_31).
date_split(d2012_12_31,2012,12,31).

year(2013).
date(d2013_01_01).
date_split(d2013_01_01,2013,1,1).
date(d2013_12_31).
date_split(d2013_12_31,2013,12,31).

year(2014).
date(d2014_07_09).
date_split(d2014_07_09,2014,7,9).
date(d2014_01_01).
date_split(d2014_01_01,2014,1,1).
date(d2014_12_31).
date_split(d2014_12_31,2014,12,31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01,2015,1,1).
date(d2015_12_31).
date_split(d2015_12_31,2015,12,31).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01,2016,1,1).
date(d2016_12_31).
date_split(d2016_12_31,2016,12,31).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

year(2018).
date(d2018_02_14).
date_split(d2018_02_14,2018,2,14).
date(d2018_01_01).
date_split(d2018_01_01,2018,1,1).
date(d2018_12_31).
date_split(d2018_12_31,2018,12,31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01,2019,1,1).
date(d2019_12_31).
date_split(d2019_12_31,2019,12,31).

atom_concat('bob_maintains_household_s2_b_1_A_pos',2004,bob_maintains_household_s2_b_1_A_pos2004).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2005,bob_maintains_household_s2_b_1_A_pos2005).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2006,bob_maintains_household_s2_b_1_A_pos2006).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2007,bob_maintains_household_s2_b_1_A_pos2007).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2008,bob_maintains_household_s2_b_1_A_pos2008).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2009,bob_maintains_household_s2_b_1_A_pos2009).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2010,bob_maintains_household_s2_b_1_A_pos2010).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2011,bob_maintains_household_s2_b_1_A_pos2011).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2012,bob_maintains_household_s2_b_1_A_pos2012).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2013,bob_maintains_household_s2_b_1_A_pos2013).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2014,bob_maintains_household_s2_b_1_A_pos2014).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2015,bob_maintains_household_s2_b_1_A_pos2015).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2016,bob_maintains_household_s2_b_1_A_pos2016).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2017,bob_maintains_household_s2_b_1_A_pos2017).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2018,bob_maintains_household_s2_b_1_A_pos2018).
atom_concat('bob_maintains_household_s2_b_1_A_pos',2019,bob_maintains_household_s2_b_1_A_pos2019).

finance(1).

marriage_(alice_and_bob_s2_b_1_A_pos).
agent_(alice_and_bob_s2_b_1_A_pos,alice_s2_b_1_A_pos).
agent_(alice_and_bob_s2_b_1_A_pos,bob_s2_b_1_A_pos).
start_(alice_and_bob_s2_b_1_A_pos,d1992_02_03).
death_(alice_dies_s2_b_1_A_pos).
agent_(alice_dies_s2_b_1_A_pos,alice_s2_b_1_A_pos).
start_(alice_dies_s2_b_1_A_pos,d2014_07_09).
end_(alice_dies_s2_b_1_A_pos,d2014_07_09).
son_(charlie_is_son_s2_b_1_A_pos).
agent_(charlie_is_son_s2_b_1_A_pos,charlie_s2_b_1_A_pos).
patient_(charlie_is_son_s2_b_1_A_pos,alice_s2_b_1_A_pos).
patient_(charlie_is_son_s2_b_1_A_pos,bob_s2_b_1_A_pos).
start_(charlie_is_son_s2_b_1_A_pos,d2000_10_09).
residence_(charlie_and_bob_residence_s2_b_1_A_pos).
agent_(charlie_and_bob_residence_s2_b_1_A_pos,charlie_s2_b_1_A_pos).
agent_(charlie_and_bob_residence_s2_b_1_A_pos,bob_s2_b_1_A_pos).
patient_(charlie_and_bob_residence_s2_b_1_A_pos,bob_s_house_s2_b_1_A_pos).
start_(charlie_and_bob_residence_s2_b_1_A_pos,d2004_01_01).
end_(charlie_and_bob_residence_s2_b_1_A_pos,d2019_12_31).
bob_household_maintenance(Year,Event,Start_day,End_day) :-
    between(2004,2019,Year),
    atom_concat('bob_maintains_household_s2_b_1_A_pos',Year,Event),
    first_day_year(Year,Start_day),
    last_day_year(Year,End_day).
payment_(Event) :- bob_household_maintenance(_,Event,_,_).
agent_(Event,bob_s2_b_1_A_pos) :- bob_household_maintenance(_,Event,_,_).
amount_(Event,1) :- bob_household_maintenance(_,Event,_,_).
purpose_(Event,bob_s_house_s2_b_1_A_pos) :- bob_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- bob_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- bob_household_maintenance(_,Event,_,End_day).
s152_c(charlie_s2_b_1_A_pos,bob_s2_b_1_A_pos,Year) :- between(2004,2019,Year).

% Test
:- s2_b_1_A(bob_s2_b_1_A_pos,bob_s_house_s2_b_1_A_pos,charlie_s2_b_1_A_pos,2018).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice and Bob have a child, Charlie, born October 9th, 2000. Alice died on July 9th, 2014. From 2004 to 2019, Bob furnished the costs of maintaining the home where he and Charlie lived during that time. Bob is entitled to a deduction for Charlie under section 151(c) for the years 2015 to 2019.

% Question
% Section 2(b)(1)(B) applies to Bob in 2018. Contradiction

% Facts
person(alice_s2_b_1_B_neg).
person(bob_s2_b_1_B_neg).
person(charlie_s2_b_1_B_neg).

year(1992).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).

year(2000).
date(d2000_10_09).
date_split(d2000_10_09,2000,10,9).
date(d2000_01_01).
date_split(d2000_01_01,2000,1,1).
date(d2000_12_31).
date_split(d2000_12_31,2000,12,31).

year(2004).
date(d2004_01_01).
date_split(d2004_01_01,2004,1,1).
date(d2004_12_31).
date_split(d2004_12_31,2004,12,31).

year(2005).
date(d2005_01_01).
date_split(d2005_01_01,2005,1,1).
date(d2005_12_31).
date_split(d2005_12_31,2005,12,31).

year(2006).
date(d2006_01_01).
date_split(d2006_01_01,2006,1,1).
date(d2006_12_31).
date_split(d2006_12_31,2006,12,31).

year(2007).
date(d2007_01_01).
date_split(d2007_01_01,2007,1,1).
date(d2007_12_31).
date_split(d2007_12_31,2007,12,31).

year(2008).
date(d2008_01_01).
date_split(d2008_01_01,2008,1,1).
date(d2008_12_31).
date_split(d2008_12_31,2008,12,31).

year(2009).
date(d2009_01_01).
date_split(d2009_01_01,2009,1,1).
date(d2009_12_31).
date_split(d2009_12_31,2009,12,31).

year(2010).
date(d2010_01_01).
date_split(d2010_01_01,2010,1,1).
date(d2010_12_31).
date_split(d2010_12_31,2010,12,31).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01,2011,1,1).
date(d2011_12_31).
date_split(d2011_12_31,2011,12,31).

year(2012).
date(d2012_01_01).
date_split(d2012_01_01,2012,1,1).
date(d2012_12_31).
date_split(d2012_12_31,2012,12,31).

year(2013).
date(d2013_01_01).
date_split(d2013_01_01,2013,1,1).
date(d2013_12_31).
date_split(d2013_12_31,2013,12,31).

year(2014).
date(d2014_07_09).
date_split(d2014_07_09,2014,7,9).
date(d2014_01_01).
date_split(d2014_01_01,2014,1,1).
date(d2014_12_31).
date_split(d2014_12_31,2014,12,31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01,2015,1,1).
date(d2015_12_31).
date_split(d2015_12_31,2015,12,31).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01,2016,1,1).
date(d2016_12_31).
date_split(d2016_12_31,2016,12,31).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

year(2018).
date(d2018_02_14).
date_split(d2018_02_14,2018,2,14).
date(d2018_01_01).
date_split(d2018_01_01,2018,1,1).
date(d2018_12_31).
date_split(d2018_12_31,2018,12,31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01,2019,1,1).
date(d2019_12_31).
date_split(d2019_12_31,2019,12,31).

atom_concat('bob_maintains_household_s2_b_1_B_neg',2004,bob_maintains_household_s2_b_1_B_neg2004).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2005,bob_maintains_household_s2_b_1_B_neg2005).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2006,bob_maintains_household_s2_b_1_B_neg2006).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2007,bob_maintains_household_s2_b_1_B_neg2007).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2008,bob_maintains_household_s2_b_1_B_neg2008).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2009,bob_maintains_household_s2_b_1_B_neg2009).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2010,bob_maintains_household_s2_b_1_B_neg2010).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2011,bob_maintains_household_s2_b_1_B_neg2011).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2012,bob_maintains_household_s2_b_1_B_neg2012).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2013,bob_maintains_household_s2_b_1_B_neg2013).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2014,bob_maintains_household_s2_b_1_B_neg2014).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2015,bob_maintains_household_s2_b_1_B_neg2015).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2016,bob_maintains_household_s2_b_1_B_neg2016).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2017,bob_maintains_household_s2_b_1_B_neg2017).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2018,bob_maintains_household_s2_b_1_B_neg2018).
atom_concat('bob_maintains_household_s2_b_1_B_neg',2019,bob_maintains_household_s2_b_1_B_neg2019).

finance(1).

marriage_(alice_and_bob_s2_b_1_B_neg).
agent_(alice_and_bob_s2_b_1_B_neg,alice_s2_b_1_B_neg).
agent_(alice_and_bob_s2_b_1_B_neg,bob_s2_b_1_B_neg).
start_(alice_and_bob_s2_b_1_B_neg,d1992_02_03).
death_(alice_dies_s2_b_1_B_neg).
agent_(alice_dies_s2_b_1_B_neg,alice_s2_b_1_B_neg).
start_(alice_dies_s2_b_1_B_neg,d2014_07_09).
end_(alice_dies_s2_b_1_B_neg,d2014_07_09).
son_(charlie_is_son_s2_b_1_B_neg).
agent_(charlie_is_son_s2_b_1_B_neg,charlie_s2_b_1_B_neg).
patient_(charlie_is_son_s2_b_1_B_neg,alice_s2_b_1_B_neg).
patient_(charlie_is_son_s2_b_1_B_neg,bob_s2_b_1_B_neg).
start_(charlie_is_son_s2_b_1_B_neg,d2000_10_09).
residence_(charlie_and_bob_residence_s2_b_1_B_neg).
agent_(charlie_and_bob_residence_s2_b_1_B_neg,charlie_s2_b_1_B_neg).
agent_(charlie_and_bob_residence_s2_b_1_B_neg,bob_s2_b_1_B_neg).
patient_(charlie_and_bob_residence_s2_b_1_B_neg,bob_s_house_s2_b_1_B_neg).
start_(charlie_and_bob_residence_s2_b_1_B_neg,d2004_01_01).
end_(charlie_and_bob_residence_s2_b_1_B_neg,d2019_12_31).
bob_household_maintenance(Year,Event,Start_day,End_day) :-
    between(2004,2019,Year),
    atom_concat('bob_maintains_household_s2_b_1_B_neg',Year,Event),
    first_day_year(Year,Start_day),
    last_day_year(Year,End_day).
payment_(Event) :- bob_household_maintenance(_,Event,_,_).
agent_(Event,bob_s2_b_1_B_neg) :- bob_household_maintenance(_,Event,_,_).
amount_(Event,1) :- bob_household_maintenance(_,Event,_,_).
purpose_(Event,bob_s_house_s2_b_1_B_neg) :- bob_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- bob_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- bob_household_maintenance(_,Event,_,End_day).
s151_c_applies(bob_s2_b_1_B_neg,charlie_s2_b_1_B_neg,Year) :- between(2015,2019,Year).

% Test
:- \+ s2_b_1_B(bob_s2_b_1_B_neg,bob_s_house_s2_b_1_B_neg,charlie_s2_b_1_B_neg,0,2018).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice died on July 9th, 2014. From 2004 to 2019, Bob furnished the costs of maintaining the home where he and and his father Charlie lived during that time. Bob is entitled to a deduction for Charlie under section 151(c) for the years 2015 to 2019.

% Question
% Section 2(b)(1)(B) applies to Bob in 2018. Entailment

% Facts
person(alice_s2_b_1_B_pos).
person(bob_s2_b_1_B_pos).
person(charlie_s2_b_1_B_pos).

year(1992).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).

year(2000).
date(d2000_10_09).
date_split(d2000_10_09,2000,10,9).
date(d2000_01_01).
date_split(d2000_01_01,2000,1,1).
date(d2000_12_31).
date_split(d2000_12_31,2000,12,31).

year(2004).
date(d2004_01_01).
date_split(d2004_01_01,2004,1,1).
date(d2004_12_31).
date_split(d2004_12_31,2004,12,31).

year(2005).
date(d2005_01_01).
date_split(d2005_01_01,2005,1,1).
date(d2005_12_31).
date_split(d2005_12_31,2005,12,31).

year(2006).
date(d2006_01_01).
date_split(d2006_01_01,2006,1,1).
date(d2006_12_31).
date_split(d2006_12_31,2006,12,31).

year(2007).
date(d2007_01_01).
date_split(d2007_01_01,2007,1,1).
date(d2007_12_31).
date_split(d2007_12_31,2007,12,31).

year(2008).
date(d2008_01_01).
date_split(d2008_01_01,2008,1,1).
date(d2008_12_31).
date_split(d2008_12_31,2008,12,31).

year(2009).
date(d2009_01_01).
date_split(d2009_01_01,2009,1,1).
date(d2009_12_31).
date_split(d2009_12_31,2009,12,31).

year(2010).
date(d2010_01_01).
date_split(d2010_01_01,2010,1,1).
date(d2010_12_31).
date_split(d2010_12_31,2010,12,31).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01,2011,1,1).
date(d2011_12_31).
date_split(d2011_12_31,2011,12,31).

year(2012).
date(d2012_01_01).
date_split(d2012_01_01,2012,1,1).
date(d2012_12_31).
date_split(d2012_12_31,2012,12,31).

year(2013).
date(d2013_01_01).
date_split(d2013_01_01,2013,1,1).
date(d2013_12_31).
date_split(d2013_12_31,2013,12,31).

year(2014).
date(d2014_07_09).
date_split(d2014_07_09,2014,7,9).
date(d2014_01_01).
date_split(d2014_01_01,2014,1,1).
date(d2014_12_31).
date_split(d2014_12_31,2014,12,31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01,2015,1,1).
date(d2015_12_31).
date_split(d2015_12_31,2015,12,31).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01,2016,1,1).
date(d2016_12_31).
date_split(d2016_12_31,2016,12,31).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

year(2018).
date(d2018_02_14).
date_split(d2018_02_14,2018,2,14).
date(d2018_01_01).
date_split(d2018_01_01,2018,1,1).
date(d2018_12_31).
date_split(d2018_12_31,2018,12,31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01,2019,1,1).
date(d2019_12_31).
date_split(d2019_12_31,2019,12,31).

atom_concat('bob_maintains_household_s2_b_1_B_pos',2004,bob_maintains_household_s2_b_1_B_pos2004).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2005,bob_maintains_household_s2_b_1_B_pos2005).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2006,bob_maintains_household_s2_b_1_B_pos2006).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2007,bob_maintains_household_s2_b_1_B_pos2007).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2008,bob_maintains_household_s2_b_1_B_pos2008).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2009,bob_maintains_household_s2_b_1_B_pos2009).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2010,bob_maintains_household_s2_b_1_B_pos2010).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2011,bob_maintains_household_s2_b_1_B_pos2011).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2012,bob_maintains_household_s2_b_1_B_pos2012).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2013,bob_maintains_household_s2_b_1_B_pos2013).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2014,bob_maintains_household_s2_b_1_B_pos2014).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2015,bob_maintains_household_s2_b_1_B_pos2015).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2016,bob_maintains_household_s2_b_1_B_pos2016).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2017,bob_maintains_household_s2_b_1_B_pos2017).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2018,bob_maintains_household_s2_b_1_B_pos2018).
atom_concat('bob_maintains_household_s2_b_1_B_pos',2019,bob_maintains_household_s2_b_1_B_pos2019).

finance(1).

marriage_(alice_and_bob_s2_b_1_B_pos).
agent_(alice_and_bob_s2_b_1_B_pos,alice_s2_b_1_B_pos).
agent_(alice_and_bob_s2_b_1_B_pos,bob_s2_b_1_B_pos).
start_(alice_and_bob_s2_b_1_B_pos,d1992_02_03).
death_(alice_dies_s2_b_1_B_pos).
agent_(alice_dies_s2_b_1_B_pos,alice_s2_b_1_B_pos).
start_(alice_dies_s2_b_1_B_pos,d2014_07_09).
end_(alice_dies_s2_b_1_B_pos,d2014_07_09).
father_(charlie_is_father_s2_b_1_B_pos).
agent_(charlie_is_father_s2_b_1_B_pos,charlie_s2_b_1_B_pos).
patient_(charlie_is_father_s2_b_1_B_pos,bob_s2_b_1_B_pos).
residence_(charlie_and_bob_residence_s2_b_1_B_pos).
agent_(charlie_and_bob_residence_s2_b_1_B_pos,charlie_s2_b_1_B_pos).
agent_(charlie_and_bob_residence_s2_b_1_B_pos,bob_s2_b_1_B_pos).
patient_(charlie_and_bob_residence_s2_b_1_B_pos,bob_s_house_s2_b_1_B_pos).
start_(charlie_and_bob_residence_s2_b_1_B_pos,d2004_01_01).
end_(charlie_and_bob_residence_s2_b_1_B_pos,d2019_12_31).
bob_household_maintenance(Year,Event,Start_day,End_day) :-
    between(2004,2019,Year),
    atom_concat('bob_maintains_household_s2_b_1_B_pos',Year,Event),
    first_day_year(Year,Start_day),
    last_day_year(Year,End_day).
payment_(Event) :- bob_household_maintenance(_,Event,_,_).
agent_(Event,bob_s2_b_1_B_pos) :- bob_household_maintenance(_,Event,_,_).
amount_(Event,1) :- bob_household_maintenance(_,Event,_,_).
purpose_(Event,bob_s_house_s2_b_1_B_pos) :- bob_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- bob_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- bob_household_maintenance(_,Event,_,End_day).
s151_c_applies(bob_s2_b_1_B_pos,charlie_s2_b_1_B_pos,Year) :- between(2015,2019,Year).

% Test
:- s2_b_1_B(bob_s2_b_1_B_pos,bob_s_house_s2_b_1_B_pos,charlie_s2_b_1_B_pos,0,2018).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice died on July 9th, 2014. From 2004 to 2019, Bob furnished the costs of maintaining the home where he and his son Charlie lived during that time. Bob is entitled to a deduction for Charlie under section 151(c) for the years 2015 to 2019.

% Question
% Section 2(b)(1) applies to Bob in 2016. Contradiction

% Facts
person(alice_s2_b_1_neg).
person(bob_s2_b_1_neg).
person(charlie_s2_b_1_neg).

year(1992).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).

year(2000).
date(d2000_01_01).
date_split(d2000_01_01,2000,1,1).
date(d2000_12_31).
date_split(d2000_12_31,2000,12,31).

year(2004).
date(d2004_01_01).
date_split(d2004_01_01,2004,1,1).
date(d2004_12_31).
date_split(d2004_12_31,2004,12,31).

year(2005).
date(d2005_01_01).
date_split(d2005_01_01,2005,1,1).
date(d2005_12_31).
date_split(d2005_12_31,2005,12,31).

year(2006).
date(d2006_01_01).
date_split(d2006_01_01,2006,1,1).
date(d2006_12_31).
date_split(d2006_12_31,2006,12,31).

year(2007).
date(d2007_01_01).
date_split(d2007_01_01,2007,1,1).
date(d2007_12_31).
date_split(d2007_12_31,2007,12,31).

year(2008).
date(d2008_01_01).
date_split(d2008_01_01,2008,1,1).
date(d2008_12_31).
date_split(d2008_12_31,2008,12,31).

year(2009).
date(d2009_01_01).
date_split(d2009_01_01,2009,1,1).
date(d2009_12_31).
date_split(d2009_12_31,2009,12,31).

year(2010).
date(d2010_01_01).
date_split(d2010_01_01,2010,1,1).
date(d2010_12_31).
date_split(d2010_12_31,2010,12,31).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01,2011,1,1).
date(d2011_12_31).
date_split(d2011_12_31,2011,12,31).

year(2012).
date(d2012_01_01).
date_split(d2012_01_01,2012,1,1).
date(d2012_12_31).
date_split(d2012_12_31,2012,12,31).

year(2013).
date(d2013_01_01).
date_split(d2013_01_01,2013,1,1).
date(d2013_12_31).
date_split(d2013_12_31,2013,12,31).

year(2014).
date(d2014_07_09).
date_split(d2014_07_09,2014,7,9).
date(d2014_01_01).
date_split(d2014_01_01,2014,1,1).
date(d2014_12_31).
date_split(d2014_12_31,2014,12,31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01,2015,1,1).
date(d2015_12_31).
date_split(d2015_12_31,2015,12,31).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01,2016,1,1).
date(d2016_12_31).
date_split(d2016_12_31,2016,12,31).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

year(2018).
date(d2018_02_14).
date_split(d2018_02_14,2018,2,14).
date(d2018_01_01).
date_split(d2018_01_01,2018,1,1).
date(d2018_12_31).
date_split(d2018_12_31,2018,12,31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01,2019,1,1).
date(d2019_12_31).
date_split(d2019_12_31,2019,12,31).

atom_concat('bob_maintains_household_s2_b_1_neg',2004,bob_maintains_household_s2_b_1_neg2004).
atom_concat('bob_maintains_household_s2_b_1_neg',2005,bob_maintains_household_s2_b_1_neg2005).
atom_concat('bob_maintains_household_s2_b_1_neg',2006,bob_maintains_household_s2_b_1_neg2006).
atom_concat('bob_maintains_household_s2_b_1_neg',2007,bob_maintains_household_s2_b_1_neg2007).
atom_concat('bob_maintains_household_s2_b_1_neg',2008,bob_maintains_household_s2_b_1_neg2008).
atom_concat('bob_maintains_household_s2_b_1_neg',2009,bob_maintains_household_s2_b_1_neg2009).
atom_concat('bob_maintains_household_s2_b_1_neg',2010,bob_maintains_household_s2_b_1_neg2010).
atom_concat('bob_maintains_household_s2_b_1_neg',2011,bob_maintains_household_s2_b_1_neg2011).
atom_concat('bob_maintains_household_s2_b_1_neg',2012,bob_maintains_household_s2_b_1_neg2012).
atom_concat('bob_maintains_household_s2_b_1_neg',2013,bob_maintains_household_s2_b_1_neg2013).
atom_concat('bob_maintains_household_s2_b_1_neg',2014,bob_maintains_household_s2_b_1_neg2014).
atom_concat('bob_maintains_household_s2_b_1_neg',2015,bob_maintains_household_s2_b_1_neg2015).
atom_concat('bob_maintains_household_s2_b_1_neg',2016,bob_maintains_household_s2_b_1_neg2016).
atom_concat('bob_maintains_household_s2_b_1_neg',2017,bob_maintains_household_s2_b_1_neg2017).
atom_concat('bob_maintains_household_s2_b_1_neg',2018,bob_maintains_household_s2_b_1_neg2018).
atom_concat('bob_maintains_household_s2_b_1_neg',2019,bob_maintains_household_s2_b_1_neg2019).

finance(1).

marriage_(alice_and_bob_s2_b_1_neg).
agent_(alice_and_bob_s2_b_1_neg,alice_s2_b_1_neg).
agent_(alice_and_bob_s2_b_1_neg,bob_s2_b_1_neg).
start_(alice_and_bob_s2_b_1_neg,d1992_02_03).
death_(alice_dies_s2_b_1_neg).
agent_(alice_dies_s2_b_1_neg,alice_s2_b_1_neg).
start_(alice_dies_s2_b_1_neg,d2014_07_09).
end_(alice_dies_s2_b_1_neg,d2014_07_09).
son_(charlie_is_son_s2_b_1_neg).
agent_(charlie_is_son_s2_b_1_neg,charlie_s2_b_1_neg).
patient_(charlie_is_son_s2_b_1_neg,bob_s2_b_1_neg).
residence_(charlie_and_bob_residence_s2_b_1_neg).
agent_(charlie_and_bob_residence_s2_b_1_neg,charlie_s2_b_1_neg).
agent_(charlie_and_bob_residence_s2_b_1_neg,bob_s2_b_1_neg).
patient_(charlie_and_bob_residence_s2_b_1_neg,bob_s_house_s2_b_1_neg).
start_(charlie_and_bob_residence_s2_b_1_neg,d2004_01_01).
end_(charlie_and_bob_residence_s2_b_1_neg,d2019_12_31).
bob_household_maintenance(Year,Event,Start_day,End_day) :-
    between(2004,2019,Year),
    atom_concat('bob_maintains_household_s2_b_1_neg',Year,Event),
    first_day_year(Year,Start_day),
    last_day_year(Year,End_day).
payment_(Event) :- bob_household_maintenance(_,Event,_,_).
agent_(Event,bob_s2_b_1_neg) :- bob_household_maintenance(_,Event,_,_).
amount_(Event,1) :- bob_household_maintenance(_,Event,_,_).
purpose_(Event,bob_s_house_s2_b_1_neg) :- bob_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- bob_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- bob_household_maintenance(_,Event,_,End_day).
s151_c_applies(bob_s2_b_1_neg,charlie_s2_b_1_neg,Year) :- between(2015,2019,Year).

% Test
:- \+ s2_b_1(bob_s2_b_1_neg,bob_s_house_s2_b_1_neg,charlie_s2_b_1_neg,2016).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice died on July 9th, 2014. From 2004 to 2019, Bob furnished the costs of maintaining the home where he and and his father Charlie lived during that time. Bob is entitled to a deduction for Charlie under section 151(c) for the years 2015 to 2019.

% Question
% Section 2(b)(1) applies to Bob in 2018. Entailment

% Facts
person(alice_s2_b_1_pos).
person(bob_s2_b_1_pos).
person(charlie_s2_b_1_pos).

year(1992).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).

year(2000).
date(d2000_01_01).
date_split(d2000_01_01,2000,1,1).
date(d2000_12_31).
date_split(d2000_12_31,2000,12,31).

year(2004).
date(d2004_01_01).
date_split(d2004_01_01,2004,1,1).
date(d2004_12_31).
date_split(d2004_12_31,2004,12,31).

year(2005).
date(d2005_01_01).
date_split(d2005_01_01,2005,1,1).
date(d2005_12_31).
date_split(d2005_12_31,2005,12,31).

year(2006).
date(d2006_01_01).
date_split(d2006_01_01,2006,1,1).
date(d2006_12_31).
date_split(d2006_12_31,2006,12,31).

year(2007).
date(d2007_01_01).
date_split(d2007_01_01,2007,1,1).
date(d2007_12_31).
date_split(d2007_12_31,2007,12,31).

year(2008).
date(d2008_01_01).
date_split(d2008_01_01,2008,1,1).
date(d2008_12_31).
date_split(d2008_12_31,2008,12,31).

year(2009).
date(d2009_01_01).
date_split(d2009_01_01,2009,1,1).
date(d2009_12_31).
date_split(d2009_12_31,2009,12,31).

year(2010).
date(d2010_01_01).
date_split(d2010_01_01,2010,1,1).
date(d2010_12_31).
date_split(d2010_12_31,2010,12,31).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01,2011,1,1).
date(d2011_12_31).
date_split(d2011_12_31,2011,12,31).

year(2012).
date(d2012_01_01).
date_split(d2012_01_01,2012,1,1).
date(d2012_12_31).
date_split(d2012_12_31,2012,12,31).

year(2013).
date(d2013_01_01).
date_split(d2013_01_01,2013,1,1).
date(d2013_12_31).
date_split(d2013_12_31,2013,12,31).

year(2014).
date(d2014_07_09).
date_split(d2014_07_09,2014,7,9).
date(d2014_01_01).
date_split(d2014_01_01,2014,1,1).
date(d2014_12_31).
date_split(d2014_12_31,2014,12,31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01,2015,1,1).
date(d2015_12_31).
date_split(d2015_12_31,2015,12,31).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01,2016,1,1).
date(d2016_12_31).
date_split(d2016_12_31,2016,12,31).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

year(2018).
date(d2018_02_14).
date_split(d2018_02_14,2018,2,14).
date(d2018_01_01).
date_split(d2018_01_01,2018,1,1).
date(d2018_12_31).
date_split(d2018_12_31,2018,12,31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01,2019,1,1).
date(d2019_12_31).
date_split(d2019_12_31,2019,12,31).

atom_concat('bob_maintains_household_s2_b_1_pos',2004,bob_maintains_household_s2_b_1_pos2004).
atom_concat('bob_maintains_household_s2_b_1_pos',2005,bob_maintains_household_s2_b_1_pos2005).
atom_concat('bob_maintains_household_s2_b_1_pos',2006,bob_maintains_household_s2_b_1_pos2006).
atom_concat('bob_maintains_household_s2_b_1_pos',2007,bob_maintains_household_s2_b_1_pos2007).
atom_concat('bob_maintains_household_s2_b_1_pos',2008,bob_maintains_household_s2_b_1_pos2008).
atom_concat('bob_maintains_household_s2_b_1_pos',2009,bob_maintains_household_s2_b_1_pos2009).
atom_concat('bob_maintains_household_s2_b_1_pos',2010,bob_maintains_household_s2_b_1_pos2010).
atom_concat('bob_maintains_household_s2_b_1_pos',2011,bob_maintains_household_s2_b_1_pos2011).
atom_concat('bob_maintains_household_s2_b_1_pos',2012,bob_maintains_household_s2_b_1_pos2012).
atom_concat('bob_maintains_household_s2_b_1_pos',2013,bob_maintains_household_s2_b_1_pos2013).
atom_concat('bob_maintains_household_s2_b_1_pos',2014,bob_maintains_household_s2_b_1_pos2014).
atom_concat('bob_maintains_household_s2_b_1_pos',2015,bob_maintains_household_s2_b_1_pos2015).
atom_concat('bob_maintains_household_s2_b_1_pos',2016,bob_maintains_household_s2_b_1_pos2016).
atom_concat('bob_maintains_household_s2_b_1_pos',2017,bob_maintains_household_s2_b_1_pos2017).
atom_concat('bob_maintains_household_s2_b_1_pos',2018,bob_maintains_household_s2_b_1_pos2018).
atom_concat('bob_maintains_household_s2_b_1_pos',2019,bob_maintains_household_s2_b_1_pos2019).

finance(1).

marriage_(alice_and_bob_s2_b_1_pos).
agent_(alice_and_bob_s2_b_1_pos,alice_s2_b_1_pos).
agent_(alice_and_bob_s2_b_1_pos,bob_s2_b_1_pos).
start_(alice_and_bob_s2_b_1_pos,d1992_02_03).
death_(alice_dies_s2_b_1_pos).
agent_(alice_dies_s2_b_1_pos,alice_s2_b_1_pos).
start_(alice_dies_s2_b_1_pos,d2014_07_09).
end_(alice_dies_s2_b_1_pos,d2014_07_09).
father_(charlie_is_father_s2_b_1_pos).
agent_(charlie_is_father_s2_b_1_pos,charlie_s2_b_1_pos).
patient_(charlie_is_father_s2_b_1_pos,bob_s2_b_1_pos).
residence_(charlie_and_bob_residence_s2_b_1_pos).
agent_(charlie_and_bob_residence_s2_b_1_pos,charlie_s2_b_1_pos).
agent_(charlie_and_bob_residence_s2_b_1_pos,bob_s2_b_1_pos).
patient_(charlie_and_bob_residence_s2_b_1_pos,bob_s_house_s2_b_1_pos).
start_(charlie_and_bob_residence_s2_b_1_pos,d2004_01_01).
end_(charlie_and_bob_residence_s2_b_1_pos,d2019_12_31).
bob_household_maintenance(Year,Event,Start_day,End_day) :-
    between(2004,2019,Year),
    atom_concat('bob_maintains_household_s2_b_1_pos',Year,Event),
    first_day_year(Year,Start_day),
    last_day_year(Year,End_day).
payment_(Event) :- bob_household_maintenance(_,Event,_,_).
agent_(Event,bob_s2_b_1_pos) :- bob_household_maintenance(_,Event,_,_).
amount_(Event,1) :- bob_household_maintenance(_,Event,_,_).
purpose_(Event,bob_s_house_s2_b_1_pos) :- bob_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- bob_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- bob_household_maintenance(_,Event,_,End_day).
s151_c_applies(bob_s2_b_1_pos,charlie_s2_b_1_pos,Year) :- between(2015,2019,Year).

% Test
:- s2_b_1(bob_s2_b_1_pos,bob_s_house_s2_b_1_pos,charlie_s2_b_1_pos,2018).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice and Bob were legally separated under a decree of separate maintenance on July 9th, 2014.

% Question
% Section 2(b)(2)(A) applies to Alice and Bob in 2010. Contradiction

% Facts
person(alice_s2_b_2_A_neg).
person(bob_s2_b_2_A_neg).

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

year(2010).

marriage_(alice_and_bob_s2_b_2_A_neg).
agent_(alice_and_bob_s2_b_2_A_neg,alice_s2_b_2_A_neg).
agent_(alice_and_bob_s2_b_2_A_neg,bob_s2_b_2_A_neg).
start_(alice_and_bob_s2_b_2_A_neg,d1992_02_03).
legal_separation_(alice_and_bob_divorce_s2_b_2_A_neg).
agent_(alice_and_bob_divorce_s2_b_2_A_neg,"decree of separate maintenance").
patient_(alice_and_bob_divorce_s2_b_2_A_neg,alice_and_bob_s2_b_2_A_neg).
start_(alice_and_bob_divorce_s2_b_2_A_neg,d2014_07_09).

% Test
:- \+ s2_b_2_A(alice_s2_b_2_A_neg,bob_s2_b_2_A_neg,alice_and_bob_divorce_s2_b_2_A_neg,alice_and_bob_s2_b_2_A_neg,2010).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice and Bob were legally separated under a decree of separate maintenance on July 9th, 2014.

% Question
% Section 2(b)(2)(A) applies to Alice and Bob in 2018. Entailment

% Facts
person(alice_s2_b_2_A_pos).
person(bob_s2_b_2_A_pos).

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

year(2018).

marriage_(alice_and_bob_s2_b_2_A_pos).
agent_(alice_and_bob_s2_b_2_A_pos,alice_s2_b_2_A_pos).
agent_(alice_and_bob_s2_b_2_A_pos,bob_s2_b_2_A_pos).
start_(alice_and_bob_s2_b_2_A_pos,d1992_02_03).
legal_separation_(alice_and_bob_divorce_s2_b_2_A_pos).
agent_(alice_and_bob_divorce_s2_b_2_A_pos,"decree of separate maintenance").
patient_(alice_and_bob_divorce_s2_b_2_A_pos,alice_and_bob_s2_b_2_A_pos).
start_(alice_and_bob_divorce_s2_b_2_A_pos,d2014_07_09).

% Test
:- s2_b_2_A(alice_s2_b_2_A_pos,bob_s2_b_2_A_pos,alice_and_bob_divorce_s2_b_2_A_pos,alice_and_bob_s2_b_2_A_pos,2018).
:- halt.
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
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice was a nonresident alien until July 9th, 2014.

% Question
% Section 2(b)(2)(B) applies to Bob in 2013. Entailment

% Facts
person(alice_s2_b_2_B_pos).
person(bob_s2_b_2_B_pos).

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

year(2013).

marriage_(alice_and_bob_s2_b_2_B_pos).
agent_(alice_and_bob_s2_b_2_B_pos,alice_s2_b_2_B_pos).
agent_(alice_and_bob_s2_b_2_B_pos,bob_s2_b_2_B_pos).
start_(alice_and_bob_s2_b_2_B_pos,d1992_02_03).
nonresident_alien_(alice_is_a_nra_s2_b_2_B_pos).
agent_(alice_is_a_nra_s2_b_2_B_pos,alice_s2_b_2_B_pos).
end_(alice_is_a_nra_s2_b_2_B_pos,d2014_07_09).

% Test
:- s2_b_2_B(bob_s2_b_2_B_pos,alice_s2_b_2_B_pos,2013).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice was a nonresident alien. Alice died on July 9th, 2014.

% Question
% Section 2(b)(2)(C) applies to Bob in 2014. Contradiction

% Facts
person(alice_s2_b_2_C_neg).
person(bob_s2_b_2_C_neg).

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

year(2014).

marriage_(alice_and_bob_s2_b_2_C_neg).
agent_(alice_and_bob_s2_b_2_C_neg,alice_s2_b_2_C_neg).
agent_(alice_and_bob_s2_b_2_C_neg,bob_s2_b_2_C_neg).
start_(alice_and_bob_s2_b_2_C_neg,d1992_02_03).
death_(alice_dies_s2_b_2_C_neg).
agent_(alice_dies_s2_b_2_C_neg,alice_s2_b_2_C_neg).
start_(alice_dies_s2_b_2_C_neg,d2014_07_09).
end_(alice_dies_s2_b_2_C_neg,d2014_07_09).
nonresident_alien_(alice_is_a_nra_s2_b_2_C_neg).
agent_(alice_is_a_nra_s2_b_2_C_neg,alice_s2_b_2_C_neg).

% Test
:- \+ s2_b_2_C(bob_s2_b_2_C_neg,alice_and_bob_s2_b_2_C_neg,alice_s2_b_2_C_neg,2014).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice died on July 9th, 2014.

% Question
% Section 2(b)(2)(C) applies to Bob in 2014. Entailment

% Facts
person(alice_s2_b_2_C_pos).
person(bob_s2_b_2_C_pos).

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

year(2014).

marriage_(alice_and_bob_s2_b_2_C_pos).
agent_(alice_and_bob_s2_b_2_C_pos,alice_s2_b_2_C_pos).
agent_(alice_and_bob_s2_b_2_C_pos,bob_s2_b_2_C_pos).
start_(alice_and_bob_s2_b_2_C_pos,d1992_02_03).
death_(alice_dies_s2_b_2_C_pos).
agent_(alice_dies_s2_b_2_C_pos,alice_s2_b_2_C_pos).
start_(alice_dies_s2_b_2_C_pos,d2014_07_09).
end_(alice_dies_s2_b_2_C_pos,d2014_07_09).

% Test
:- s2_b_2_C(bob_s2_b_2_C_pos,alice_and_bob_s2_b_2_C_pos,alice_s2_b_2_C_pos,2014).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice died on July 9th, 2014. From 2004 to 2019, Bob furnished the costs of maintaining the home where he and and his father Charlie lived during that time. Bob is entitled to a deduction for Charlie under section 151(c) for the years 2015 to 2019.

% Question
% Section 2(b)(3)(B) applies to Bob in 2018. Contradiction

% Facts
person(alice_s2_b_3_B_neg).
person(bob_s2_b_3_B_neg).
person(charlie_s2_b_3_B_neg).

year(1992).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).

year(2000).
date(d2000_01_01).
date_split(d2000_01_01,2000,1,1).
date(d2000_12_31).
date_split(d2000_12_31,2000,12,31).

year(2004).
date(d2004_01_01).
date_split(d2004_01_01,2004,1,1).
date(d2004_12_31).
date_split(d2004_12_31,2004,12,31).

year(2005).
date(d2005_01_01).
date_split(d2005_01_01,2005,1,1).
date(d2005_12_31).
date_split(d2005_12_31,2005,12,31).

year(2006).
date(d2006_01_01).
date_split(d2006_01_01,2006,1,1).
date(d2006_12_31).
date_split(d2006_12_31,2006,12,31).

year(2007).
date(d2007_01_01).
date_split(d2007_01_01,2007,1,1).
date(d2007_12_31).
date_split(d2007_12_31,2007,12,31).

year(2008).
date(d2008_01_01).
date_split(d2008_01_01,2008,1,1).
date(d2008_12_31).
date_split(d2008_12_31,2008,12,31).

year(2009).
date(d2009_01_01).
date_split(d2009_01_01,2009,1,1).
date(d2009_12_31).
date_split(d2009_12_31,2009,12,31).

year(2010).
date(d2010_01_01).
date_split(d2010_01_01,2010,1,1).
date(d2010_12_31).
date_split(d2010_12_31,2010,12,31).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01,2011,1,1).
date(d2011_12_31).
date_split(d2011_12_31,2011,12,31).

year(2012).
date(d2012_01_01).
date_split(d2012_01_01,2012,1,1).
date(d2012_12_31).
date_split(d2012_12_31,2012,12,31).

year(2013).
date(d2013_01_01).
date_split(d2013_01_01,2013,1,1).
date(d2013_12_31).
date_split(d2013_12_31,2013,12,31).

year(2014).
date(d2014_07_09).
date_split(d2014_07_09,2014,7,9).
date(d2014_01_01).
date_split(d2014_01_01,2014,1,1).
date(d2014_12_31).
date_split(d2014_12_31,2014,12,31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01,2015,1,1).
date(d2015_12_31).
date_split(d2015_12_31,2015,12,31).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01,2016,1,1).
date(d2016_12_31).
date_split(d2016_12_31,2016,12,31).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

year(2018).
date(d2018_01_01).
date_split(d2018_01_01,2018,1,1).
date(d2018_12_31).
date_split(d2018_12_31,2018,12,31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01,2019,1,1).
date(d2019_12_31).
date_split(d2019_12_31,2019,12,31).

atom_concat('bob_maintains_household_s2_b_3_B_neg', 2015, bob_maintains_household_s2_b_3_B_neg2015).
atom_concat('bob_maintains_household_s2_b_3_B_neg', 2016, bob_maintains_household_s2_b_3_B_neg2016).
atom_concat('bob_maintains_household_s2_b_3_B_neg', 2017, bob_maintains_household_s2_b_3_B_neg2017).
atom_concat('bob_maintains_household_s2_b_3_B_neg', 2018, bob_maintains_household_s2_b_3_B_neg2018).
atom_concat('bob_maintains_household_s2_b_3_B_neg', 2019, bob_maintains_household_s2_b_3_B_neg2019).

finance(1).

marriage_(alice_and_bob_s2_b_3_B_neg).
agent_(alice_and_bob_s2_b_3_B_neg,alice_s2_b_3_B_neg).
agent_(alice_and_bob_s2_b_3_B_neg,bob_s2_b_3_B_neg).
start_(alice_and_bob_s2_b_3_B_neg,d1992_02_03).
death_(alice_dies_s2_b_3_B_neg).
agent_(alice_dies_s2_b_3_B_neg,alice_s2_b_3_B_neg).
start_(alice_dies_s2_b_3_B_neg,d2014_07_09).
end_(alice_dies_s2_b_3_B_neg,d2014_07_09).
son_(charlie_is_father_s2_b_3_B_neg).
agent_(charlie_is_father_s2_b_3_B_neg,charlie_s2_b_3_B_neg).
patient_(charlie_is_father_s2_b_3_B_neg,bob_s2_b_3_B_neg).
residence_(charlie_and_bob_residence_s2_b_3_B_neg).
agent_(charlie_and_bob_residence_s2_b_3_B_neg,charlie_s2_b_3_B_neg).
agent_(charlie_and_bob_residence_s2_b_3_B_neg,bob_s2_b_3_B_neg).
patient_(charlie_and_bob_residence_s2_b_3_B_neg,bob_s_house_s2_b_3_B_neg).
start_(charlie_and_bob_residence_s2_b_3_B_neg,d2004_01_01).
end_(charlie_and_bob_residence_s2_b_3_B_neg,d2019_12_31).
bob_household_maintenance(Year,Event,Start_day,End_day) :-
    between(2015,2019,Year),
    atom_concat('bob_maintains_household_s2_b_3_B_neg',Year,Event),
    first_day_year(Year,Start_day),
    last_day_year(Year,End_day).
payment_(Event) :- bob_household_maintenance(_,Event,_,_).
agent_(Event,bob_s2_b_3_B_neg) :- bob_household_maintenance(_,Event,_,_).
amount_(Event,1) :- bob_household_maintenance(_,Event,_,_).
purpose_(Event,bob_s_house_s2_b_3_B_neg) :- bob_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- bob_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- bob_household_maintenance(_,Event,_,End_day).
s151_c_applies(bob_s2_b_3_B_neg,charlie_s2_b_3_B_neg,Year) :- between(2015,2019,Year).

% Test
:- \+ s2_b_3_B(bob_s2_b_3_B_neg,charlie_s2_b_3_B_neg,2018).
:- halt.
% Text
% Alice and Bob got married on Feb 3rd, 1992. Alice died on July 9th, 2014. From 2015 to 2019, Bob furnished the costs of maintaining the home where he and and his friend Charlie lived during that time. Charlie is a dependent of Bob under section 152(d)(2)(H) for the years 2015 to 2019. Bob earned $300000 every year from 2015 to 2019.

% Question
% Section 2(b)(3)(B) applies to Bob as the taxpayer and Charlie as the individual in 2018. Entailment

% Facts
person(alice_s2_b_3_B_pos).
person(bob_s2_b_3_B_pos).
person(charlie_s2_b_3_B_pos).

year(1992).
date(d1992_02_03).
date_split(d1992_02_03,1992,2,3).
date(d1992_01_01).
date_split(d1992_01_01,1992,1,1).
date(d1992_12_31).
date_split(d1992_12_31,1992,12,31).

year(2000).
date(d2000_01_01).
date_split(d2000_01_01,2000,1,1).
date(d2000_12_31).
date_split(d2000_12_31,2000,12,31).

year(2004).
date(d2004_01_01).
date_split(d2004_01_01,2004,1,1).
date(d2004_12_31).
date_split(d2004_12_31,2004,12,31).

year(2005).
date(d2005_01_01).
date_split(d2005_01_01,2005,1,1).
date(d2005_12_31).
date_split(d2005_12_31,2005,12,31).

year(2006).
date(d2006_01_01).
date_split(d2006_01_01,2006,1,1).
date(d2006_12_31).
date_split(d2006_12_31,2006,12,31).

year(2007).
date(d2007_01_01).
date_split(d2007_01_01,2007,1,1).
date(d2007_12_31).
date_split(d2007_12_31,2007,12,31).

year(2008).
date(d2008_01_01).
date_split(d2008_01_01,2008,1,1).
date(d2008_12_31).
date_split(d2008_12_31,2008,12,31).

year(2009).
date(d2009_01_01).
date_split(d2009_01_01,2009,1,1).
date(d2009_12_31).
date_split(d2009_12_31,2009,12,31).

year(2010).
date(d2010_01_01).
date_split(d2010_01_01,2010,1,1).
date(d2010_12_31).
date_split(d2010_12_31,2010,12,31).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01,2011,1,1).
date(d2011_12_31).
date_split(d2011_12_31,2011,12,31).

year(2012).
date(d2012_01_01).
date_split(d2012_01_01,2012,1,1).
date(d2012_12_31).
date_split(d2012_12_31,2012,12,31).

year(2013).
date(d2013_01_01).
date_split(d2013_01_01,2013,1,1).
date(d2013_12_31).
date_split(d2013_12_31,2013,12,31).

year(2014).
date(d2014_07_09).
date_split(d2014_07_09,2014,7,9).
date(d2014_01_01).
date_split(d2014_01_01,2014,1,1).
date(d2014_12_31).
date_split(d2014_12_31,2014,12,31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01,2015,1,1).
date(d2015_12_31).
date_split(d2015_12_31,2015,12,31).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01,2016,1,1).
date(d2016_12_31).
date_split(d2016_12_31,2016,12,31).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

year(2018).
date(d2018_01_01).
date_split(d2018_01_01,2018,1,1).
date(d2018_12_31).
date_split(d2018_12_31,2018,12,31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01,2019,1,1).
date(d2019_12_31).
date_split(d2019_12_31,2019,12,31).

atom_concat('bob_maintains_household_s2_b_3_B_pos',2015,bob_maintains_household_s2_b_3_B_pos2015).
atom_concat('bob_maintains_household_s2_b_3_B_pos',2016,bob_maintains_household_s2_b_3_B_pos2016).
atom_concat('bob_maintains_household_s2_b_3_B_pos',2017,bob_maintains_household_s2_b_3_B_pos2017).
atom_concat('bob_maintains_household_s2_b_3_B_pos',2018,bob_maintains_household_s2_b_3_B_pos2018).
atom_concat('bob_maintains_household_s2_b_3_B_pos',2019,bob_maintains_household_s2_b_3_B_pos2019).

atom_concat('bob_income_s2_b_3_B_pos',2015,bob_income_s2_b_3_B_pos2015).
atom_concat('bob_income_s2_b_3_B_pos',2016,bob_income_s2_b_3_B_pos2016_s2_b_3_B_pos).
atom_concat('bob_income_s2_b_3_B_pos',2017,bob_income_s2_b_3_B_pos2017).
atom_concat('bob_income_s2_b_3_B_pos',2018,bob_income_s2_b_3_B_pos2018).
atom_concat('bob_income_s2_b_3_B_pos',2019,bob_income_s2_b_3_B_pos2019).

finance(1).
finance(300000).

marriage_(alice_and_bob_s2_b_3_B_pos).
agent_(alice_and_bob_s2_b_3_B_pos,alice_s2_b_3_B_pos).
agent_(alice_and_bob_s2_b_3_B_pos,bob_s2_b_3_B_pos).
start_(alice_and_bob_s2_b_3_B_pos,d1992_02_03).
death_(alice_dies_s2_b_3_B_pos).
agent_(alice_dies_s2_b_3_B_pos,alice_s2_b_3_B_pos).
start_(alice_dies_s2_b_3_B_pos,d2014_07_09).
end_(alice_dies_s2_b_3_B_pos,d2014_07_09).
residence_(charlie_and_bob_residence_s2_b_3_B_pos).
agent_(charlie_and_bob_residence_s2_b_3_B_pos,charlie_s2_b_3_B_pos).
agent_(charlie_and_bob_residence_s2_b_3_B_pos,bob_s2_b_3_B_pos).
patient_(charlie_and_bob_residence_s2_b_3_B_pos,bob_s_house_s2_b_3_B_pos).
start_(charlie_and_bob_residence_s2_b_3_B_pos,d2004_01_01).
end_(charlie_and_bob_residence_s2_b_3_B_pos,d2019_12_31).
bob_household_maintenance(Year,Event,Start_day,End_day) :-
    between(2015,2019,Year),
    atom_concat('bob_maintains_household_s2_b_3_B_pos',Year,Event),
    first_day_year(Year,Start_day),
    last_day_year(Year,End_day).
payment_(Event) :- bob_household_maintenance(_,Event,_,_).
agent_(Event,bob_s2_b_3_B_pos) :- bob_household_maintenance(_,Event,_,_).
amount_(Event,1) :- bob_household_maintenance(_,Event,_,_).
purpose_(Event,bob_s_house_s2_b_3_B_pos) :- bob_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- bob_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- bob_household_maintenance(_,Event,_,End_day).
s152_d_2_H(charlie_s2_b_3_B_pos,bob_s2_b_3_B_pos,Year,_,Start_day,End_day) :-
    between(2015,2019,Year),first_day_year(Year,Start_day),last_day_year(Year,End_day).
bob_income(Year,Event,Start_day,End_day) :-
    between(2015,2019,Year),
    atom_concat('bob_income_s2_b_3_B_pos',Year,Event),
    first_day_year(Year,Start_day),
    last_day_year(Year,End_day).
income_(Event) :- bob_household_maintenance(_,Event,_,_).
agent_(Event,bob_s2_b_3_B_pos) :- bob_household_maintenance(_,Event,_,_).
amount_(Event,300000) :- bob_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- bob_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- bob_household_maintenance(_,Event,_,End_day).

% Test
:- s2_b_3_B(bob_s2_b_3_B_pos,charlie_s2_b_3_B_pos,2018).
:- halt.
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

s3306_b(3200,3200,bob_works_s3306_a_1_A_neg,alice_s3306_a_1_A_neg,bob_s3306_a_1_A_neg,alice_s3306_a_1_A_neg,bob_s3306_a_1_A_neg,"cash").
start_(bob_works_s3306_a_1_A_neg,d2017_02_01).
end_(bob_works_s3306_a_1_A_neg,d2017_09_02).
s3306_b(4500,4500,alice_works_s3306_a_1_A_neg,bob_s3306_a_1_A_neg,alice_s3306_a_1_A_neg,bob_s3306_a_1_A_neg,alice_s3306_a_1_A_neg,"cash").
start_(alice_works_s3306_a_1_A_neg,d2017_04_01).
end_(alice_works_s3306_a_1_A_neg,d2018_09_02).

% Test
:- \+ s3306_a_1_A(alice_s3306_a_1_A_neg,2019,3200).
:- halt.
% Text
% Alice has paid wages of $3200 to Bob for work done from Feb 1st, 2017 to Sep 2nd, 2017. Bob has paid wages of $4500 to Alice for work done from Apr 1st, 2017 to Sep 2nd, 2018.

% Question
% Section 3306(a)(1)(A) make Alice an employer for the year 2017. Entailment

% Facts
person(alice_s3306_a_1_A_pos).
person(bob_s3306_a_1_A_pos).
finance(3200).
finance(4500).

year(2017).
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


s3306_b(3200,3200,bob_works_s3306_a_1_A_pos,alice_s3306_a_1_A_pos,bob_s3306_a_1_A_pos,alice_s3306_a_1_A_pos,bob_s3306_a_1_A_pos,"cash").
start_(bob_works_s3306_a_1_A_pos,d2017_02_01).
end_(bob_works_s3306_a_1_A_pos,d2017_09_02).
s3306_b(4500,4500,alice_works_s3306_a_1_A_pos,bob_s3306_a_1_A_pos,alice_s3306_a_1_A_pos,bob_s3306_a_1_A_pos,alice_s3306_a_1_A_pos,"cash").
start_(alice_works_s3306_a_1_A_pos,d2017_04_01).
end_(alice_works_s3306_a_1_A_pos,d2018_09_02).

% Test
:- s3306_a_1_A(alice_s3306_a_1_A_pos,2017,3200).
:- halt.
% Text
% Alice has paid $3200 to Bob for domestic service done from Feb 1st, 2017 to Sep 2nd, 2017. Bob has paid $4500 to Alice for work done from Apr 1st, 2017 to Sep 2nd, 2018.

% Question
% Alice is an employer under section 3306(a)(1) for the year 2018. Contradiction

% Facts
person(alice_s3306_a_1_neg).
person(bob_s3306_a_1_neg).

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

service_(alice_employer_s3306_a_1_neg).
patient_(alice_employer_s3306_a_1_neg,alice_s3306_a_1_neg).
agent_(alice_employer_s3306_a_1_neg,bob_s3306_a_1_neg).
start_(alice_employer_s3306_a_1_neg,d2017_02_01).
end_(alice_employer_s3306_a_1_neg,d2017_09_02).
purpose_(alice_employer_s3306_a_1_neg,"domestic service").
payment_(alice_pays_s3306_a_1_neg).
agent_(alice_pays_s3306_a_1_neg,alice_s3306_a_1_neg).
patient_(alice_pays_s3306_a_1_neg,bob_s3306_a_1_neg).
start_(alice_pays_s3306_a_1_neg,d2019_09_02).
purpose_(alice_pays_s3306_a_1_neg,alice_employer_s3306_a_1_neg).
amount_(alice_pays_s3306_a_1_neg,3200).
s3306_b(3200,alice_pays_s3306_a_1_neg,alice_employer_s3306_a_1_neg,alice_s3306_a_1_neg,bob_s3306_a_1_neg,alice_s3306_a_1_neg,bob_s3306_a_1_neg,_).
service_(bob_employer_s3306_a_1_neg).
patient_(bob_employer_s3306_a_1_neg,bob_s3306_a_1_neg).
agent_(bob_employer_s3306_a_1_neg,alice_s3306_a_1_neg).
start_(bob_employer_s3306_a_1_neg,d2017_02_01).
end_(bob_employer_s3306_a_1_neg,d2017_09_02).
payment_(bob_pays_s3306_a_1_neg).
agent_(bob_pays_s3306_a_1_neg,bob_s3306_a_1_neg).
patient_(bob_pays_s3306_a_1_neg,alice_s3306_a_1_neg).
start_(bob_pays_s3306_a_1_neg,d2018_09_02).
purpose_(bob_pays_s3306_a_1_neg,bob_employer_s3306_a_1_neg).
amount_(bob_pays_s3306_a_1_neg,4500).
s3306_b(4500,bob_pays_s3306_a_1_neg,bob_employer_s3306_a_1_neg,bob_s3306_a_1_neg,alice_s3306_a_1_neg,bob_s3306_a_1_neg,alice_s3306_a_1_neg,_).

% Test
:- \+ s3306_a_1(alice_s3306_a_1_neg,2018).
:- halt.
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
purpose_(alice_employer_s3306_a_1_pos,"domestic service").
payment_(alice_pays_s3306_a_1_pos).
agent_(alice_pays_s3306_a_1_pos,alice_s3306_a_1_pos).
patient_(alice_pays_s3306_a_1_pos,bob_s3306_a_1_pos).
start_(alice_pays_s3306_a_1_pos,d2019_09_02).
purpose_(alice_pays_s3306_a_1_pos,alice_employer_s3306_a_1_pos).
amount_(alice_pays_s3306_a_1_pos,3200).
s3306_b(3200,alice_pays_s3306_a_1_pos,alice_employer_s3306_a_1_pos,alice_s3306_a_1_pos,bob_s3306_a_1_pos,alice_s3306_a_1_pos,bob_s3306_a_1_pos,"cash").
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
s3306_b(4500,bob_pays_s3306_a_1_pos,bob_employer_s3306_a_1_pos,bob_s3306_a_1_pos,alice_s3306_a_1_pos,bob_s3306_a_1_pos,alice_s3306_a_1_pos,"cash").

% Test
:- s3306_a_1(bob_s3306_a_1_pos,2018).
:- halt.
% Text
% Alice has paid wages of $3200 to Bob for agricultural labor done from Feb 1st, 2017 to Sep 2nd, 2017. Bob has paid wages of $4520 to Alice for work done from Apr 1st, 2017 to Sep 2nd, 2018.

% Question
% Section 3306(a)(2)(A) make Alice an employer for the year 2017. Contradiction

% Facts
person(alice_s3306_a_2_A_neg).
person(bob_s3306_a_2_A_neg).

year(2017).
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

% year(2019).
% date(d2019_01_01).
% date_split(d2019_01_01, 2019, 1, 1).
% date(d2019_09_02).
% date_split(d2019_09_02, 2019, 9, 2).
% date(d2019_12_31).
% date_split(d2019_12_31, 2019, 12, 31).

year(2018).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_09_02).
date_split(d2018_09_02, 2018, 9, 2).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

finance(3200).
finance(4520).

service_(alice_employer_s3306_a_2_A_neg).
patient_(alice_employer_s3306_a_2_A_neg,alice_s3306_a_2_A_neg).
agent_(alice_employer_s3306_a_2_A_neg,bob_s3306_a_2_A_neg).
start_(alice_employer_s3306_a_2_A_neg,d2017_02_01).
end_(alice_employer_s3306_a_2_A_neg,d2017_09_02).
purpose_(alice_employer_s3306_a_2_A_neg,"agricultural labor").
payment_(alice_pays_s3306_a_2_A_neg).
agent_(alice_pays_s3306_a_2_A_neg,alice_s3306_a_2_A_neg).
patient_(alice_pays_s3306_a_2_A_neg,bob_s3306_a_2_A_neg).
start_(alice_pays_s3306_a_2_A_neg,d2017_09_02).
purpose_(alice_pays_s3306_a_2_A_neg,alice_employer_s3306_a_2_A_neg).
amount_(alice_pays_s3306_a_2_A_neg,3200).
s3306_b(3200,alice_pays_s3306_a_2_A_neg,alice_employer_s3306_a_2_A_neg,alice_s3306_a_2_A_neg,bob_s3306_a_2_A_neg,alice_s3306_a_2_A_neg,bob_s3306_a_2_A_neg,"cash").
service_(bob_employer_s3306_a_2_A_neg).
patient_(bob_employer_s3306_a_2_A_neg,bob_s3306_a_2_A_neg).
agent_(bob_employer_s3306_a_2_A_neg,alice_s3306_a_2_A_neg).
start_(bob_employer_s3306_a_2_A_neg,d2017_04_01).
end_(bob_employer_s3306_a_2_A_neg,d2018_09_02).
payment_(bob_pays_s3306_a_2_A_neg).
agent_(bob_pays_s3306_a_2_A_neg,bob_s3306_a_2_A_neg).
patient_(bob_pays_s3306_a_2_A_neg,alice_s3306_a_2_A_neg).
start_(bob_pays_s3306_a_2_A_neg,d2018_09_02).
purpose_(bob_pays_s3306_a_2_A_neg,bob_employer_s3306_a_2_A_neg).
amount_(bob_pays_s3306_a_2_A_neg,4520).
s3306_b(4520,bob_pays_s3306_a_2_A_neg,bob_employer_s3306_a_2_A_neg,bob_s3306_a_2_A_neg,alice_s3306_a_2_A_neg,bob_s3306_a_2_A_neg,alice_s3306_a_2_A_neg,"cash").

% Test
:- \+ s3306_a_2_A(alice_s3306_a_2_A_neg,2017,3200,alice_employer_s3306_a_2_A_neg).
:- halt.
% Text
% Alice has paid wages of $6771, $6954, $6872 to Bob, Charlie and Dan respectively for agricultural labor done from Feb 1st, 2017 to Sep 2nd, 2017. Bob has paid wages of $4520 to Alice for work done from Apr 1st, 2017 to Sep 2nd, 2018.

% Question
% Section 3306(a)(2)(A) make Alice an employer for the year 2017. Entailment

% Facts
person(alice_s3306_a_2_A_pos).
person(bob_s3306_a_2_A_pos).
person(charlie_s3306_a_2_A_pos).
person(dan_s3306_a_2_A_pos).

year(2017).
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
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_09_02).
date_split(d2018_09_02, 2018, 9, 2).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

finance(4520).
finance(6771).
finance(6954).
finance(6872).
medium("cash").

service_(alice_employer_bob_s3306_a_2_A_pos).
patient_(alice_employer_bob_s3306_a_2_A_pos,alice_s3306_a_2_A_pos).
agent_(alice_employer_bob_s3306_a_2_A_pos,bob_s3306_a_2_A_pos).
start_(alice_employer_bob_s3306_a_2_A_pos,d2017_02_01).
end_(alice_employer_bob_s3306_a_2_A_pos,d2017_09_02).
purpose_(alice_employer_bob_s3306_a_2_A_pos,"agricultural labor").
payment_(alice_pays_bob_s3306_a_2_A_pos).
agent_(alice_pays_bob_s3306_a_2_A_pos,alice_s3306_a_2_A_pos).
patient_(alice_pays_bob_s3306_a_2_A_pos,bob_s3306_a_2_A_pos).
start_(alice_pays_bob_s3306_a_2_A_pos,d2017_09_02).
purpose_(alice_pays_bob_s3306_a_2_A_pos,alice_employer_bob_s3306_a_2_A_pos).
amount_(alice_pays_bob_s3306_a_2_A_pos,6771).
s3306_b(6771,alice_pays_bob_s3306_a_2_A_pos,alice_employer_bob_s3306_a_2_A_pos,alice_s3306_a_2_A_pos,bob_s3306_a_2_A_pos,alice_s3306_a_2_A_pos,bob_s3306_a_2_A_pos,"cash").
service_(alice_employer_charlie_s3306_a_2_A_pos).
patient_(alice_employer_charlie_s3306_a_2_A_pos,alice_s3306_a_2_A_pos).
agent_(alice_employer_charlie_s3306_a_2_A_pos,charlie_s3306_a_2_A_pos).
start_(alice_employer_charlie_s3306_a_2_A_pos,d2017_02_01).
end_(alice_employer_charlie_s3306_a_2_A_pos,d2017_09_02).
purpose_(alice_employer_charlie_s3306_a_2_A_pos,"agricultural labor").
payment_(alice_pays_charlie_s3306_a_2_A_pos).
agent_(alice_pays_charlie_s3306_a_2_A_pos,alice_s3306_a_2_A_pos).
patient_(alice_pays_charlie_s3306_a_2_A_pos,charlie_s3306_a_2_A_pos).
start_(alice_pays_charlie_s3306_a_2_A_pos,d2017_09_02).
purpose_(alice_pays_charlie_s3306_a_2_A_pos,alice_employer_charlie_s3306_a_2_A_pos).
amount_(alice_pays_charlie_s3306_a_2_A_pos,6954).
s3306_b(6954,alice_pays_charlie_s3306_a_2_A_pos,alice_employer_charlie_s3306_a_2_A_pos,alice_s3306_a_2_A_pos,charlie_s3306_a_2_A_pos,alice_s3306_a_2_A_pos,charlie_s3306_a_2_A_pos,_).
service_(alice_employer_dan_s3306_a_2_A_pos).
patient_(alice_employer_dan_s3306_a_2_A_pos,alice_s3306_a_2_A_pos).
agent_(alice_employer_dan_s3306_a_2_A_pos,dan_s3306_a_2_A_pos).
start_(alice_employer_dan_s3306_a_2_A_pos,d2017_02_01).
end_(alice_employer_dan_s3306_a_2_A_pos,d2017_09_02).
purpose_(alice_employer_dan_s3306_a_2_A_pos,"agricultural labor").
payment_(alice_pays_dan_s3306_a_2_A_pos).
agent_(alice_pays_dan_s3306_a_2_A_pos,alice_s3306_a_2_A_pos).
patient_(alice_pays_dan_s3306_a_2_A_pos,dan_s3306_a_2_A_pos).
start_(alice_pays_dan_s3306_a_2_A_pos,d2017_09_02).
purpose_(alice_pays_dan_s3306_a_2_A_pos,alice_employer_dan_s3306_a_2_A_pos).
amount_(alice_pays_dan_s3306_a_2_A_pos,6872).
s3306_b(6872,alice_pays_dan_s3306_a_2_A_pos,alice_employer_dan_s3306_a_2_A_pos,alice_s3306_a_2_A_pos,dan_s3306_a_2_A_pos,alice_s3306_a_2_A_pos,dan_s3306_a_2_A_pos,_).
service_(bob_employer_s3306_a_2_A_pos).
patient_(bob_employer_s3306_a_2_A_pos,bob_s3306_a_2_A_pos).
agent_(bob_employer_s3306_a_2_A_pos,alice_s3306_a_2_A_pos).
start_(bob_employer_s3306_a_2_A_pos,d2017_04_01).
end_(bob_employer_s3306_a_2_A_pos,d2018_09_02).
payment_(bob_pays_s3306_a_2_A_pos).
agent_(bob_pays_s3306_a_2_A_pos,bob_s3306_a_2_A_pos).
patient_(bob_pays_s3306_a_2_A_pos,alice_s3306_a_2_A_pos).
start_(bob_pays_s3306_a_2_A_pos,d2018_09_02).
end_(bob_pays_s3306_a_2_A_pos,d2018_09_02).
purpose_(bob_pays_s3306_a_2_A_pos,bob_employer_s3306_a_2_A_pos).
amount_(bob_pays_s3306_a_2_A_pos,4520).
s3306_b(4520,bob_pays_s3306_a_2_A_pos,bob_employer_s3306_a_2_A_pos,bob_s3306_a_2_A_pos,alice_s3306_a_2_A_pos,bob_s3306_a_2_A_pos,alice_s3306_a_2_A_pos,"cash").

% Test
:- s3306_a_2_A(alice_s3306_a_2_A_pos,2017,6771,alice_employer_bob_s3306_a_2_A_pos),s3306_a_2_A(alice_s3306_a_2_A_pos,2017,6954,alice_employer_charlie_s3306_a_2_A_pos),s3306_a_2_A(alice_s3306_a_2_A_pos,2017,6872,alice_employer_dan_s3306_a_2_A_pos).
:- halt.
% Text
% Alice has employed Bob, Cameron, Dan, Emily, Fred and George for agricultural labor on various occasions during the year 2017:
% - Jan 24: B, C, D, E and F
% - Feb 4: B, C and F
% - Mar 3: B, C, D, E and F
% - Mar 19: C, D, E, F and G
% - Apr 2: B, C, D, F and G
% - May 9: C, D, E, F and G
% - Oct 15: B, C, D, E and G
% - Oct 25: B, E, F and G
% - Nov 8: B, C, E, F and G
% - Nov 22: B, C, D, E and F
% - Dec 1: B, C, D, E and G
% - Dec 3: B, C, D, E and G

% Question
% Section 3306(a)(2)(B) applies to Alice for the year 2017. Contradiction

% Facts
person(alice_s3306_a_2_B_neg).
person(bob_s3306_a_2_B_neg).
person(cameron_s3306_a_2_B_neg).
person(dan_s3306_a_2_B_neg).
person(emily_s3306_a_2_B_neg).
person(fred_s3306_a_2_B_neg).
person(george_s3306_a_2_B_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).
date(d2017_01_24).
date_split(d2017_01_24, 2017, 1, 24).
date(d2017_02_04).
date_split(d2017_02_04, 2017, 2, 4).
date(d2017_03_03).
date_split(d2017_03_03, 2017, 3, 3).
date(d2017_03_19).
date_split(d2017_03_19, 2017, 3, 19).
date(d2017_04_02).
date_split(d2017_04_02, 2017, 4, 2).
date(d2017_05_09).
date_split(d2017_05_09, 2017, 5, 9).
date(d2017_10_15).
date_split(d2017_10_15, 2017, 10, 15).
date(d2017_10_25).
date_split(d2017_10_25, 2017, 10, 25).
date(d2017_11_08).
date_split(d2017_11_08, 2017, 11, 8).
date(d2017_11_22).
date_split(d2017_11_22, 2017, 11, 22).
date(d2017_12_01).
date_split(d2017_12_01, 2017, 12, 1).
date(d2017_12_03).
date_split(d2017_12_03, 2017, 12, 3).

s3306_c(alice_employer_2017-s3306_a_2_B_neg01-24,alice_s3306_a_2_B_neg,bob_s3306_a_2_B_neg,d2017_01_24,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg01-24,alice_s3306_a_2_B_neg,cameron_s3306_a_2_B_neg,d2017_01_24,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg01-24,alice_s3306_a_2_B_neg,dan_s3306_a_2_B_neg,d2017_01_24,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg01-24,alice_s3306_a_2_B_neg,emily_s3306_a_2_B_neg,d2017_01_24,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg01-24,alice_s3306_a_2_B_neg,fred_s3306_a_2_B_neg,d2017_01_24,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_neg02-04,alice_s3306_a_2_B_neg,bob_s3306_a_2_B_neg,d2017_02_04,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg02-04,alice_s3306_a_2_B_neg,cameron_s3306_a_2_B_neg,d2017_02_04,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg02-04,alice_s3306_a_2_B_neg,fred_s3306_a_2_B_neg,d2017_02_04,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_neg03-03,alice_s3306_a_2_B_neg,bob_s3306_a_2_B_neg,d2017_03_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg03-03,alice_s3306_a_2_B_neg,cameron_s3306_a_2_B_neg,d2017_03_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg03-03,alice_s3306_a_2_B_neg,dan_s3306_a_2_B_neg,d2017_03_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg03-03,alice_s3306_a_2_B_neg,emily_s3306_a_2_B_neg,d2017_03_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg03-03,alice_s3306_a_2_B_neg,fred_s3306_a_2_B_neg,d2017_03_03,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_neg03-19,alice_s3306_a_2_B_neg,cameron_s3306_a_2_B_neg,d2017_03_19,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg03-19,alice_s3306_a_2_B_neg,dan_s3306_a_2_B_neg,d2017_03_19,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg03-19,alice_s3306_a_2_B_neg,emily_s3306_a_2_B_neg,d2017_03_19,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg03-19,alice_s3306_a_2_B_neg,fred_s3306_a_2_B_neg,d2017_03_19,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg03-19,alice_s3306_a_2_B_neg,george_s3306_a_2_B_neg,d2017_03_19,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_neg04-02,alice_s3306_a_2_B_neg,bob_s3306_a_2_B_neg,d2017_04_02,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg04-02,alice_s3306_a_2_B_neg,cameron_s3306_a_2_B_neg,d2017_04_02,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg04-02,alice_s3306_a_2_B_neg,dan_s3306_a_2_B_neg,d2017_04_02,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg04-02,alice_s3306_a_2_B_neg,fred_s3306_a_2_B_neg,d2017_04_02,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg04-02,alice_s3306_a_2_B_neg,george_s3306_a_2_B_neg,d2017_04_02,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_neg05-09,alice_s3306_a_2_B_neg,cameron_s3306_a_2_B_neg,d2017_05_09,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg05-09,alice_s3306_a_2_B_neg,dan_s3306_a_2_B_neg,d2017_05_09,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg05-09,alice_s3306_a_2_B_neg,emily_s3306_a_2_B_neg,d2017_05_09,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg05-09,alice_s3306_a_2_B_neg,fred_s3306_a_2_B_neg,d2017_05_09,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg05-09,alice_s3306_a_2_B_neg,george_s3306_a_2_B_neg,d2017_05_09,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_neg10-15,alice_s3306_a_2_B_neg,bob_s3306_a_2_B_neg,d2017_10_15,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg10-15,alice_s3306_a_2_B_neg,cameron_s3306_a_2_B_neg,d2017_10_15,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg10-15,alice_s3306_a_2_B_neg,dan_s3306_a_2_B_neg,d2017_10_15,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg10-15,alice_s3306_a_2_B_neg,emily_s3306_a_2_B_neg,d2017_10_15,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg10-15,alice_s3306_a_2_B_neg,george_s3306_a_2_B_neg,d2017_10_15,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_neg10-25,alice_s3306_a_2_B_neg,bob_s3306_a_2_B_neg,d2017_10_25,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg10-25,alice_s3306_a_2_B_neg,emily_s3306_a_2_B_neg,d2017_10_25,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg10-25,alice_s3306_a_2_B_neg,fred_s3306_a_2_B_neg,d2017_10_25,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg10-25,alice_s3306_a_2_B_neg,george_s3306_a_2_B_neg,d2017_10_25,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_neg11-08,alice_s3306_a_2_B_neg,bob_s3306_a_2_B_neg,d2017_11_08,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg11-08,alice_s3306_a_2_B_neg,cameron_s3306_a_2_B_neg,d2017_11_08,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg11-08,alice_s3306_a_2_B_neg,emily_s3306_a_2_B_neg,d2017_11_08,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg11-08,alice_s3306_a_2_B_neg,fred_s3306_a_2_B_neg,d2017_11_08,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg11-08,alice_s3306_a_2_B_neg,george_s3306_a_2_B_neg,d2017_11_08,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_neg11-22,alice_s3306_a_2_B_neg,bob_s3306_a_2_B_neg,d2017_11_22,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg11-22,alice_s3306_a_2_B_neg,cameron_s3306_a_2_B_neg,d2017_11_22,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg11-22,alice_s3306_a_2_B_neg,dan_s3306_a_2_B_neg,d2017_11_22,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg11-22,alice_s3306_a_2_B_neg,emily_s3306_a_2_B_neg,d2017_11_22,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg11-22,alice_s3306_a_2_B_neg,fred_s3306_a_2_B_neg,d2017_11_22,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_neg12-01,alice_s3306_a_2_B_neg,bob_s3306_a_2_B_neg,d2017_12_01,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg12-01,alice_s3306_a_2_B_neg,cameron_s3306_a_2_B_neg,d2017_12_01,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg12-01,alice_s3306_a_2_B_neg,dan_s3306_a_2_B_neg,d2017_12_01,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg12-01,alice_s3306_a_2_B_neg,emily_s3306_a_2_B_neg,d2017_12_01,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg12-01,alice_s3306_a_2_B_neg,george_s3306_a_2_B_neg,d2017_12_01,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_neg12-03,alice_s3306_a_2_B_neg,bob_s3306_a_2_B_neg,d2017_12_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg12-03,alice_s3306_a_2_B_neg,cameron_s3306_a_2_B_neg,d2017_12_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg12-03,alice_s3306_a_2_B_neg,dan_s3306_a_2_B_neg,d2017_12_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg12-03,alice_s3306_a_2_B_neg,emily_s3306_a_2_B_neg,d2017_12_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_neg12-03,alice_s3306_a_2_B_neg,george_s3306_a_2_B_neg,d2017_12_03,2017).

% s3306_c(Service_event,alice,Employee,Day,_) :-
%     member(Day, [d2017_01_24,"2017-02-04","2017-03-03","2017-03-19","2017-04-02","2017-05-09","2017-10-15","2017-10-25","2017-11-08","2017-11-22","2017-12-01","2017-12-03"]),
%     (
%         (
%             Day == d2017_01_24,
%             member(Employee, [bob,cameron,dan,emily,fred])
%         );
%         (
%             Day == d2017_02_04,
%             member(Employee, [bob,cameron,fred])
%         );
%         (
%             Day == d2017_03_03,
%             member(Employee, [bob,cameron,dan,emily,fred])
%         );
%         (
%             Day == d2017_03_19,
%             member(Employee, [cameron,dan,emily,fred,george])
%         );
%         (
%             Day == d2017_04_02,
%             member(Employee, [bob,cameron,dan,fred,george])
%         );
%         (
%             Day == d2017_05_09,
%             member(Employee, [cameron,dan,emily,fred,george])
%         );
%         (
%             Day == d2017_10_15,
%             member(Employee, [bob,cameron,dan,emily,george])
%         );
%         (
%             Day == d2017_10_25,
%             member(Employee, [bob,emily,fred,george])
%         );
%         (
%             Day == d2017_11_08,
%             member(Employee, [bob,cameron,emily,fred,george])
%         );
%         (
%             Day == d2017_11_22,
%             member(Employee, [bob,cameron,dan,emily,fred])
%         );
%         (
%             Day == d2017_12_01,
%             member(Employee, [bob,cameron,dan,emily,george])
%         );
%         (
%             Day == d2017_12_03,
%             member(Employee, [bob,cameron,dan,emily,george])
%         )
%     ),
%     atom_concat("alice_employer_",Day,Service_event).
purpose_(alice_employer_2017-s3306_a_2_B_neg01-24,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_neg02-04,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_neg03-03,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_neg03-19,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_neg04-02,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_neg05-09,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_neg10-15,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_neg10-25,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_neg11-08,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_neg11-22,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_neg12-01,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_neg12-03,"agricultural labor").% all that's mentioned here is agricultural labor

% Test
:- \+ s3306_a_2_B(alice_s3306_a_2_B_neg,2017).
:- halt.
% Text
% Alice has employed Bob, Cameron, Dan, Emily, Fred and George for agricultural labor on various occasions during the year 2017:
% - Jan 24: B, C, D, E and F
% - Feb 4: B, C, D, E and F
% - Mar 3: B, C, D, E and F
% - Mar 19: C, D, E, F and G
% - Apr 2: B, C, D, F and G
% - May 9: C, D, E, F and G
% - Oct 15: B, C, D, E and G
% - Oct 25: B, C, D, E, F and G
% - Nov 8: B, C, E, F and G
% - Nov 22: B, C, D, E and F
% - Dec 1: B, C, D, E and G
% - Dec 3: B, C, D, E and G

% Question
% Section 3306(a)(2)(B) applies to Alice for the year 2017. Entailment

% Facts
person(alice_s3306_a_2_B_pos).
person(bob_s3306_a_2_B_pos).
person(cameron_s3306_a_2_B_pos).
person(dan_s3306_a_2_B_pos).
person(emily_s3306_a_2_B_pos).
person(fred_s3306_a_2_B_pos).
person(george_s3306_a_2_B_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).
date(d2017_01_24).
date_split(d2017_01_24, 2017, 1, 24).
date(d2017_02_04).
date_split(d2017_02_04, 2017, 2, 4).
date(d2017_03_03).
date_split(d2017_03_03, 2017, 3, 3).
date(d2017_03_19).
date_split(d2017_03_19, 2017, 3, 19).
date(d2017_04_02).
date_split(d2017_04_02, 2017, 4, 2).
date(d2017_05_09).
date_split(d2017_05_09, 2017, 5, 9).
date(d2017_10_15).
date_split(d2017_10_15, 2017, 10, 15).
date(d2017_10_25).
date_split(d2017_10_25, 2017, 10, 25).
date(d2017_11_08).
date_split(d2017_11_08, 2017, 11, 8).
date(d2017_11_22).
date_split(d2017_11_22, 2017, 11, 22).
date(d2017_12_01).
date_split(d2017_12_01, 2017, 12, 1).
date(d2017_12_03).
date_split(d2017_12_03, 2017, 12, 3).


s3306_c(alice_employer_2017-s3306_a_2_B_pos01-24,alice_s3306_a_2_B_pos,bob_s3306_a_2_B_pos,d2017_01_24,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos01-24,alice_s3306_a_2_B_pos,cameron_s3306_a_2_B_pos,d2017_01_24,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos01-24,alice_s3306_a_2_B_pos,dan_s3306_a_2_B_pos,d2017_01_24,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos01-24,alice_s3306_a_2_B_pos,emily_s3306_a_2_B_pos,d2017_01_24,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos01-24,alice_s3306_a_2_B_pos,fred_s3306_a_2_B_pos,d2017_01_24,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_pos02-04,alice_s3306_a_2_B_pos,bob_s3306_a_2_B_pos,d2017_02_04,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos02-04,alice_s3306_a_2_B_pos,cameron_s3306_a_2_B_pos,d2017_02_04,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos02-04,alice_s3306_a_2_B_pos,dan_s3306_a_2_B_pos,d2017_02_04,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos02-04,alice_s3306_a_2_B_pos,emily_s3306_a_2_B_pos,d2017_02_04,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos02-04,alice_s3306_a_2_B_pos,fred_s3306_a_2_B_pos,d2017_02_04,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_pos03-03,alice_s3306_a_2_B_pos,bob_s3306_a_2_B_pos,d2017_03_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos03-03,alice_s3306_a_2_B_pos,cameron_s3306_a_2_B_pos,d2017_03_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos03-03,alice_s3306_a_2_B_pos,dan_s3306_a_2_B_pos,d2017_03_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos03-03,alice_s3306_a_2_B_pos,emily_s3306_a_2_B_pos,d2017_03_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos03-03,alice_s3306_a_2_B_pos,fred_s3306_a_2_B_pos,d2017_03_03,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_pos03-19,alice_s3306_a_2_B_pos,cameron_s3306_a_2_B_pos,d2017_03_19,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos03-19,alice_s3306_a_2_B_pos,dan_s3306_a_2_B_pos,d2017_03_19,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos03-19,alice_s3306_a_2_B_pos,emily_s3306_a_2_B_pos,d2017_03_19,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos03-19,alice_s3306_a_2_B_pos,fred_s3306_a_2_B_pos,d2017_03_19,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos03-19,alice_s3306_a_2_B_pos,george_s3306_a_2_B_pos,d2017_03_19,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_pos04-02,alice_s3306_a_2_B_pos,bob_s3306_a_2_B_pos,d2017_04_02,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos04-02,alice_s3306_a_2_B_pos,cameron_s3306_a_2_B_pos,d2017_04_02,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos04-02,alice_s3306_a_2_B_pos,dan_s3306_a_2_B_pos,d2017_04_02,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos04-02,alice_s3306_a_2_B_pos,fred_s3306_a_2_B_pos,d2017_04_02,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos04-02,alice_s3306_a_2_B_pos,george_s3306_a_2_B_pos,d2017_04_02,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_pos05-09,alice_s3306_a_2_B_pos,cameron_s3306_a_2_B_pos,d2017_05_09,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos05-09,alice_s3306_a_2_B_pos,dan_s3306_a_2_B_pos,d2017_05_09,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos05-09,alice_s3306_a_2_B_pos,emily_s3306_a_2_B_pos,d2017_05_09,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos05-09,alice_s3306_a_2_B_pos,fred_s3306_a_2_B_pos,d2017_05_09,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos05-09,alice_s3306_a_2_B_pos,george_s3306_a_2_B_pos,d2017_05_09,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_pos10-15,alice_s3306_a_2_B_pos,bob_s3306_a_2_B_pos,d2017_10_15,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos10-15,alice_s3306_a_2_B_pos,cameron_s3306_a_2_B_pos,d2017_10_15,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos10-15,alice_s3306_a_2_B_pos,dan_s3306_a_2_B_pos,d2017_10_15,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos10-15,alice_s3306_a_2_B_pos,emily_s3306_a_2_B_pos,d2017_10_15,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos10-15,alice_s3306_a_2_B_pos,george_s3306_a_2_B_pos,d2017_10_15,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_pos10-25,alice_s3306_a_2_B_pos,bob_s3306_a_2_B_pos,d2017_10_25,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos10-25,alice_s3306_a_2_B_pos,cameron_s3306_a_2_B_pos,d2017_10_25,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos10-25,alice_s3306_a_2_B_pos,dan_s3306_a_2_B_pos,d2017_10_25,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos10-25,alice_s3306_a_2_B_pos,emily_s3306_a_2_B_pos,d2017_10_25,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos10-25,alice_s3306_a_2_B_pos,fred_s3306_a_2_B_pos,d2017_10_25,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos10-25,alice_s3306_a_2_B_pos,george_s3306_a_2_B_pos,d2017_10_25,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_pos11-08,alice_s3306_a_2_B_pos,bob_s3306_a_2_B_pos,d2017_11_08,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos11-08,alice_s3306_a_2_B_pos,cameron_s3306_a_2_B_pos,d2017_11_08,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos11-08,alice_s3306_a_2_B_pos,emily_s3306_a_2_B_pos,d2017_11_08,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos11-08,alice_s3306_a_2_B_pos,fred_s3306_a_2_B_pos,d2017_11_08,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos11-08,alice_s3306_a_2_B_pos,george_s3306_a_2_B_pos,d2017_11_08,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_pos11-22,alice_s3306_a_2_B_pos,bob_s3306_a_2_B_pos,d2017_11_22,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos11-22,alice_s3306_a_2_B_pos,cameron_s3306_a_2_B_pos,d2017_11_22,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos11-22,alice_s3306_a_2_B_pos,dan_s3306_a_2_B_pos,d2017_11_22,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos11-22,alice_s3306_a_2_B_pos,emily_s3306_a_2_B_pos,d2017_11_22,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos11-22,alice_s3306_a_2_B_pos,fred_s3306_a_2_B_pos,d2017_11_22,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_pos12-01,alice_s3306_a_2_B_pos,bob_s3306_a_2_B_pos,d2017_12_01,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos12-01,alice_s3306_a_2_B_pos,cameron_s3306_a_2_B_pos,d2017_12_01,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos12-01,alice_s3306_a_2_B_pos,dan_s3306_a_2_B_pos,d2017_12_01,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos12-01,alice_s3306_a_2_B_pos,emily_s3306_a_2_B_pos,d2017_12_01,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos12-01,alice_s3306_a_2_B_pos,george_s3306_a_2_B_pos,d2017_12_01,2017).

s3306_c(alice_employer_2017-s3306_a_2_B_pos12-03,alice_s3306_a_2_B_pos,bob_s3306_a_2_B_pos,d2017_12_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos12-03,alice_s3306_a_2_B_pos,cameron_s3306_a_2_B_pos,d2017_12_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos12-03,alice_s3306_a_2_B_pos,dan_s3306_a_2_B_pos,d2017_12_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos12-03,alice_s3306_a_2_B_pos,emily_s3306_a_2_B_pos,d2017_12_03,2017).
s3306_c(alice_employer_2017-s3306_a_2_B_pos12-03,alice_s3306_a_2_B_pos,george_s3306_a_2_B_pos,d2017_12_03,2017).

% s3306_c(Service_event,alice,Employee,Day,_) :-
%     member(Day, [d2017_01_24,"2017-02-04","2017-03-03","2017-03-19","2017-04-02","2017-05-09","2017-10-15","2017-10-25","2017-11-08","2017-11-22","2017-12-01","2017-12-03"]),
%     (
%         (
%             Day == d2017_01_24,
%             member(Employee, [bob,cameron,dan,emily,fred])
%         );
%         (
%             Day == d2017_02_04,
%             member(Employee, [bob,cameron,dan,emily,fred])
%         );
%         (
%             Day == d2017_03_03,
%             member(Employee, [bob,cameron,dan,emily,fred])
%         );
%         (
%             Day == d2017_03_19,
%             member(Employee, [cameron,dan,emily,fred,george])
%         );
%         (
%             Day == d2017_04_02,
%             member(Employee, [bob,cameron,dan,fred,george])
%         );
%         (
%             Day == d2017_05_09,
%             member(Employee, [cameron,dan,emily,fred,george])
%         );
%         (
%             Day == d2017_10_15,
%             member(Employee, [bob,cameron,dan,emily,george])
%         );
%         (
%             Day == d2017_10_25,
%             member(Employee, [bob,cameron,dan,emily,fred,george])
%         );
%         (
%             Day == d2017_11_08,
%             member(Employee, [bob,cameron,emily,fred,george])
%         );
%         (
%             Day == d2017_11_22,
%             member(Employee, [bob,cameron,dan,emily,fred])
%         );
%         (
%             Day == d2017_12_01,
%             member(Employee, [bob,cameron,dan,emily,george])
%         );
%         (
%             Day == d2017_12_03,
%             member(Employee, [bob,cameron,dan,emily,george])
%         )
%     ),
%     atom_concat("alice_employer_",Day,Service_event).
purpose_(alice_employer_2017-s3306_a_2_B_pos01-24,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_pos02-04,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_pos03-03,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_pos03-19,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_pos04-02,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_pos05-09,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_pos10-15,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_pos10-25,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_pos11-08,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_pos11-22,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_pos12-01,"agricultural labor").
purpose_(alice_employer_2017-s3306_a_2_B_pos12-03,"agricultural labor"). % all that's mentioned here is agricultural labor

% Test
:- s3306_a_2_B(alice_s3306_a_2_B_pos,2017).
:- halt.
% Text
% Alice has employed Bob from Jan 2nd, 2011 to Oct 10, 2019. On Oct 10, 2019 Bob retired because he reached age 65. Alice paid Bob $12980 as a retirement bonus.

% Question
% Section 3306(b)(10)(A) applies to the payment of $12980 that Alice made in 2019. Contradiction

% Facts
person(alice_s3306_b_10_A_neg).
person(bob_s3306_b_10_A_neg).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01, 2011, 1, 1).
date(d2011_01_02).
date_split(d2011_01_02, 2011, 1, 2).
date(d2011_12_31).
date_split(d2011_12_31, 2011, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_10_10).
date_split(d2019_10_10, 2019, 10, 10).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

finance(12980).

service_(alice_employer_s3306_b_10_A_neg).
patient_(alice_employer_s3306_b_10_A_neg,alice_s3306_b_10_A_neg).
agent_(alice_employer_s3306_b_10_A_neg,bob_s3306_b_10_A_neg).
start_(alice_employer_s3306_b_10_A_neg,d2011_01_02).
end_(alice_employer_s3306_b_10_A_neg,d2019_10_10).
termination_(alice_lays_bob_off_s3306_b_10_A_neg).
agent_(alice_lays_bob_off_s3306_b_10_A_neg,alice_s3306_b_10_A_neg).
patient_(alice_lays_bob_off_s3306_b_10_A_neg,alice_employer_s3306_b_10_A_neg).
retirement_(bob_retires_s3306_b_10_A_neg).
agent_(bob_retires_s3306_b_10_A_neg,bob_s3306_b_10_A_neg).
start_(bob_retires_s3306_b_10_A_neg,d2019_10_10).
reason_(bob_retires_s3306_b_10_A_neg,"reached age 65").
payment_(alice_pays_s3306_b_10_A_neg).
agent_(alice_pays_s3306_b_10_A_neg,alice_s3306_b_10_A_neg).
patient_(alice_pays_s3306_b_10_A_neg,bob_s3306_b_10_A_neg).
start_(alice_pays_s3306_b_10_A_neg,d2019_10_10).
purpose_(alice_pays_s3306_b_10_A_neg,alice_lays_bob_off_s3306_b_10_A_neg).
amount_(alice_pays_s3306_b_10_A_neg,12980).

% Test
:- \+ s3306_b_10_A(alice_pays_s3306_b_10_A_neg,alice_employer_s3306_b_10_A_neg,bob_s3306_b_10_A_neg,alice_s3306_b_10_A_neg,alice_lays_bob_off_s3306_b_10_A_neg,bob_retires_s3306_b_10_A_neg).
:- halt.
% Text
% Alice has employed Bob from Jan 2nd, 2011 to Oct 10, 2019. On Oct 10, 2019 Bob was diagnosed as disabled and retired. Alice paid Bob $12980 because she had to terminate their contract due to Bob's disability.

% Question
% Section 3306(b)(10)(A) applies to the payment of $12980 that Alice made in 2019. Entailment

% Facts
person(alice_s3306_b_10_A_pos).
person(bob_s3306_b_10_A_pos).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01, 2011, 1, 1).
date(d2011_01_02).
date_split(d2011_01_02, 2011, 1, 2).
date(d2011_12_31).
date_split(d2011_12_31, 2011, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_10_10).
date_split(d2019_10_10, 2019, 10, 10).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

finance(12980).

service_(alice_employer_s3306_b_10_A_pos).
patient_(alice_employer_s3306_b_10_A_pos,alice_s3306_b_10_A_pos).
agent_(alice_employer_s3306_b_10_A_pos,bob_s3306_b_10_A_pos).
start_(alice_employer_s3306_b_10_A_pos,d2011_01_02).
end_(alice_employer_s3306_b_10_A_pos,d2019_10_10).
disability_(bob_is_disabled_s3306_b_10_A_pos).
agent_(bob_is_disabled_s3306_b_10_A_pos,bob_s3306_b_10_A_pos).
start_(bob_is_disabled_s3306_b_10_A_pos,d2019_10_10).
termination_(alice_lays_bob_off_s3306_b_10_A_pos).
agent_(alice_lays_bob_off_s3306_b_10_A_pos,alice_s3306_b_10_A_pos).
patient_(alice_lays_bob_off_s3306_b_10_A_pos,alice_employer_s3306_b_10_A_pos).
reason_(alice_lays_bob_off_s3306_b_10_A_pos,bob_is_disabled_s3306_b_10_A_pos).
retirement_(bob_retires_s3306_b_10_A_pos).
agent_(bob_retires_s3306_b_10_A_pos,bob_s3306_b_10_A_pos).
start_(bob_retires_s3306_b_10_A_pos,d2019_10_10).
reason_(bob_retires_s3306_b_10_A_pos,"disability").
payment_(alice_pays_s3306_b_10_A_pos).
agent_(alice_pays_s3306_b_10_A_pos,alice_s3306_b_10_A_pos).
patient_(alice_pays_s3306_b_10_A_pos,bob_s3306_b_10_A_pos).
start_(alice_pays_s3306_b_10_A_pos,d2019_10_10).
purpose_(alice_pays_s3306_b_10_A_pos,alice_lays_bob_off_s3306_b_10_A_pos).
amount_(alice_pays_s3306_b_10_A_pos,12980).

% Test
:- s3306_b_10_A(alice_pays_s3306_b_10_A_pos,alice_employer_s3306_b_10_A_pos,bob_s3306_b_10_A_pos,alice_s3306_b_10_A_pos,alice_lays_bob_off_s3306_b_10_A_pos,bob_is_disabled_s3306_b_10_A_pos).
:- halt.
% Text
% Alice has employed Bob from Jan 2nd, 2011 to Oct 10, 2019. On Oct 10, 2019 Bob was diagnosed as disabled and retired. Alice paid Bob $12980 because she had to terminate their contract due to Bob's disability. Alice had no plan established to provide for her employees' disabilities.

% Question
% Section 3306(b)(10)(B) applies to the payment of $12980 that Alice made in 2019. Contradiction

% Facts
person(alice_s3306_b_10_B_neg).
person(bob_s3306_b_10_B_neg).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01, 2011, 1, 1).
date(d2011_01_02).
date_split(d2011_01_02, 2011, 1, 2).
date(d2011_12_31).
date_split(d2011_12_31, 2011, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_10_10).
date_split(d2019_10_10, 2019, 10, 10).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

finance(12980).

service_(alice_employer_s3306_b_10_B_neg).
patient_(alice_employer_s3306_b_10_B_neg,alice_s3306_b_10_B_neg).
agent_(alice_employer_s3306_b_10_B_neg,bob_s3306_b_10_B_neg).
start_(alice_employer_s3306_b_10_B_neg,d2011_01_02).
end_(alice_employer_s3306_b_10_B_neg,d2019_10_10).
disability_(bob_is_disabled_s3306_b_10_B_neg).
agent_(bob_is_disabled_s3306_b_10_B_neg,bob_s3306_b_10_B_neg).
start_(bob_is_disabled_s3306_b_10_B_neg,d2019_10_10).
termination_(alice_lays_bob_off_s3306_b_10_B_neg).
agent_(alice_lays_bob_off_s3306_b_10_B_neg,alice_s3306_b_10_B_neg).
patient_(alice_lays_bob_off_s3306_b_10_B_neg,alice_employer_s3306_b_10_B_neg).
reason_(alice_lays_bob_off_s3306_b_10_B_neg,bob_is_disabled_s3306_b_10_B_neg).
retirement_(bob_retires_s3306_b_10_B_neg).
agent_(bob_retires_s3306_b_10_B_neg,bob_s3306_b_10_B_neg).
start_(bob_retires_s3306_b_10_B_neg,d2019_10_10).
reason_(bob_retires_s3306_b_10_B_neg,disability).
payment_(alice_pays_s3306_b_10_B_neg).
agent_(alice_pays_s3306_b_10_B_neg,alice_s3306_b_10_B_neg).
patient_(alice_pays_s3306_b_10_B_neg,bob_s3306_b_10_B_neg).
start_(alice_pays_s3306_b_10_B_neg,d2019_10_10).
purpose_(alice_pays_s3306_b_10_B_neg,alice_lays_bob_off_s3306_b_10_B_neg).
amount_(alice_pays_s3306_b_10_B_neg,12980).

% Test
:- \+ s3306_b_10_B(alice_s3306_b_10_B_neg,alice_pays_s3306_b_10_B_neg,plan).
:- halt.
% Text
% Alice has employed Bob from Jan 2nd, 2011 to Oct 10, 2019. On Oct 10, 2019 Bob was diagnosed as disabled and retired. Alice paid Bob $12980 because she had to terminate their contract due to Bob's disability, using the disability plan set up for all of Alice's employees.

% Question
% Section 3306(b)(10)(B) applies to the payment of $12980 that Alice made in 2019. Entailment

% Facts
person(alice_s3306_b_10_B_pos).
person(bob_s3306_b_10_B_pos).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01, 2011, 1, 1).
date(d2011_01_02).
date_split(d2011_01_02, 2011, 1, 2).
date(d2011_12_31).
date_split(d2011_12_31, 2011, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_10_10).
date_split(d2019_10_10, 2019, 10, 10).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

finance(12980).

service_(alice_employer_s3306_b_10_B_pos).
patient_(alice_employer_s3306_b_10_B_pos,alice_s3306_b_10_B_pos).
agent_(alice_employer_s3306_b_10_B_pos,bob_s3306_b_10_B_pos).
start_(alice_employer_s3306_b_10_B_pos,d2011_01_02).
end_(alice_employer_s3306_b_10_B_pos,d2019_10_10).
disability_(bob_is_disabled_s3306_b_10_B_pos).
agent_(bob_is_disabled_s3306_b_10_B_pos,bob_s3306_b_10_B_pos).
start_(bob_is_disabled_s3306_b_10_B_pos,d2019_10_10).
termination_(alice_lays_bob_off_s3306_b_10_B_pos).
agent_(alice_lays_bob_off_s3306_b_10_B_pos,alice_s3306_b_10_B_pos).
patient_(alice_lays_bob_off_s3306_b_10_B_pos,alice_employer_s3306_b_10_B_pos).
reason_(alice_lays_bob_off_s3306_b_10_B_pos,bob_is_disabled_s3306_b_10_B_pos).
retirement_(bob_retires_s3306_b_10_B_pos).
agent_(bob_retires_s3306_b_10_B_pos,bob_s3306_b_10_B_pos).
start_(bob_retires_s3306_b_10_B_pos,d2019_10_10).
reason_(bob_retires_s3306_b_10_B_pos,disability).
payment_(alice_pays_s3306_b_10_B_pos).
agent_(alice_pays_s3306_b_10_B_pos,alice_s3306_b_10_B_pos).
patient_(alice_pays_s3306_b_10_B_pos,bob_s3306_b_10_B_pos).
start_(alice_pays_s3306_b_10_B_pos,d2019_10_10).
purpose_(alice_pays_s3306_b_10_B_pos,alice_lays_bob_off_s3306_b_10_B_pos).
amount_(alice_pays_s3306_b_10_B_pos,12980).
means_(alice_pays_s3306_b_10_B_pos,disability_plan_s3306_b_10_B_pos).
plan_(disability_plan_s3306_b_10_B_pos).
agent_(disability_plan_s3306_b_10_B_pos,alice_s3306_b_10_B_pos).
purpose_(disability_plan_s3306_b_10_B_pos,"make provisions for employees or dependents").


% Test
:- s3306_b_10_B(alice_s3306_b_10_B_pos,alice_pays_s3306_b_10_B_pos,disability_plan_s3306_b_10_B_pos).
:- halt.
% Text
% Alice has paid $3200 to Bob for repairing her roof from Feb 1st, 2017 to Sep 2nd, 2017. Alice paid Bob with eggs, grapes and hay.

% Question
% Section 3306(b)(11) applies to the payment that Alice made to Bob for the year 2017. Contradiction

% Facts
person(alice_s3306_b_11_neg).
person(bob_s3306_b_11_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

finance(3200).
medium("kind").

service_(alice_employer_s3306_b_11_neg).
patient_(alice_employer_s3306_b_11_neg,alice_s3306_b_11_neg).
agent_(alice_employer_s3306_b_11_neg,bob_s3306_b_11_neg).
start_(alice_employer_s3306_b_11_neg,d2017_02_01).
end_(alice_employer_s3306_b_11_neg,d2017_09_02).
payment_(alice_pays_s3306_b_11_neg).
agent_(alice_pays_s3306_b_11_neg,alice_s3306_b_11_neg).
patient_(alice_pays_s3306_b_11_neg,bob_s3306_b_11_neg).
start_(alice_pays_s3306_b_11_neg,d2017_09_02).
purpose_(alice_pays_s3306_b_11_neg,alice_employer_s3306_b_11_neg).
amount_(alice_pays_s3306_b_11_neg,3200).
means_(alice_pays_s3306_b_11_neg,"kind").

% Test
:- \+ s3306_b_11(alice_pays_s3306_b_11_neg,alice_employer_s3306_b_11_neg,"kind").
:- halt.
% Text
% Alice has paid $3200 to Bob for agricultural labor done from Feb 1st, 2017 to Sep 2nd, 2017. Alice paid Bob with eggs, grapes and hay.

% Question
% Section 3306(b)(11) applies to the payment that Alice made to Bob for the year 2017. Entailment

% Facts
person(alice_s3306_b_11_pos).
person(bob_s3306_b_11_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

finance(3200).
medium("kind").

service_(alice_employer_s3306_b_11_pos).
patient_(alice_employer_s3306_b_11_pos,alice_s3306_b_11_pos).
agent_(alice_employer_s3306_b_11_pos,bob_s3306_b_11_pos).
start_(alice_employer_s3306_b_11_pos,d2017_02_01).
end_(alice_employer_s3306_b_11_pos,d2017_09_02).
purpose_(alice_employer_s3306_b_11_pos,"agricultural labor").
payment_(alice_pays_s3306_b_11_pos).
agent_(alice_pays_s3306_b_11_pos,alice_s3306_b_11_pos).
patient_(alice_pays_s3306_b_11_pos,bob_s3306_b_11_pos).
start_(alice_pays_s3306_b_11_pos,d2017_09_02).
purpose_(alice_pays_s3306_b_11_pos,alice_employer_s3306_b_11_pos).
amount_(alice_pays_s3306_b_11_pos,3200).
means_(alice_pays_s3306_b_11_pos,"kind").

% Test
:- s3306_b_11(alice_pays_s3306_b_11_pos,alice_employer_s3306_b_11_pos,"kind").
:- halt.
% Text
% Alice employed Bob for agricultural labor from Feb 1st, 2011 to November 19th, 2019. On November 25th, Bob died from a heart attack. On December 20th, 2019, Alice paid Charlie, Bob's surviving spouse, Bob's outstanding wages of $1200.

% Question
% Section 3306(b)(15) applies to the payment that Alice made to Charlie in 2019. Contradiction

% Facts
person(alice_s3306_b_15_neg).
person(bob_s3306_b_15_neg).
person(charlie_s3306_b_15_neg).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01, 2011, 1, 1).
date(d2011_02_01).
date_split(d2011_02_01, 2011, 2, 1).
date(d2011_12_31).
date_split(d2011_12_31, 2011, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_11_19).
date_split(d2019_11_19, 2019, 11, 19).
date(d2019_11_25).
date_split(d2019_11_25, 2019, 11, 25).
date(d2019_12_20).
date_split(d2019_12_20, 2019, 12, 20).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

finance(1200).

s3306_c(alice_employer_s3306_b_15_neg,alice_s3306_b_15_neg,bob_s3306_b_15_neg,Day,Year) :-
    date_split(Day,Year,_,_),
    is_before(d2011_02_01,Day),
    is_before(Day,d2019_11_19).

purpose_(alice_employer_s3306_b_15_neg,"agricultural labor").
death_(bob_dies_s3306_b_15_neg).
agent_(bob_dies_s3306_b_15_neg,bob_s3306_b_15_neg).
start_(bob_dies_s3306_b_15_neg,d2019_11_25).
end_(bob_dies_s3306_b_15_neg,d2019_11_25).
marriage_(bob_and_charlie_s3306_b_15_neg).
agent_(bob_and_charlie_s3306_b_15_neg,bob_s3306_b_15_neg).
agent_(bob_and_charlie_s3306_b_15_neg,charlie_s3306_b_15_neg).
payment_(alice_pays_s3306_b_15_neg).
agent_(alice_pays_s3306_b_15_neg,alice_s3306_b_15_neg).
patient_(alice_pays_s3306_b_15_neg,charlie_s3306_b_15_neg).
start_(alice_pays_s3306_b_15_neg,d2019_12_20).
end_(alice_pays_s3306_b_15_neg,d2019_12_20).
purpose_(alice_pays_s3306_b_15_neg,alice_employer_s3306_b_15_neg).
amount_(alice_pays_s3306_b_15_neg,1200).

% Test
:- \+ s3306_b_15(alice_pays_s3306_b_15_neg,alice_s3306_b_15_neg,charlie_s3306_b_15_neg,bob_s3306_b_15_neg,2019).
:- halt.
% Text
% Alice employed Bob for agricultural labor from Feb 1st, 2011 to November 19th, 2019. On November 25th, Bob died from a heart attack. On January 20th, 2020, Alice paid Charlie, Bob's surviving spouse, Bob's outstanding wages of $1200.

% Question
% Section 3306(b)(15) applies to the payment that Alice made to Charlie in 2020. Entailment

% Facts
person(alice_s3306_b_15_pos).
person(bob_s3306_b_15_pos).
person(charlie_s3306_b_15_pos).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01, 2011, 1, 1).
date(d2011_02_01).
date_split(d2011_02_01, 2011, 2, 1).
date(d2011_12_31).
date_split(d2011_12_31, 2011, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_11_19).
date_split(d2019_11_19, 2019, 11, 19).
date(d2019_11_25).
date_split(d2019_11_25, 2019, 11, 25).
date(d2019_12_20).
date_split(d2019_12_20, 2019, 12, 20).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

year(2020).
date(d2020_01_01).
date_split(d2020_01_01, 2020, 1, 1).
date(d2020_01_20).
date_split(d2020_01_20, 2020, 1, 20).
date(d2020_12_31).
date_split(d2020_12_31, 2020, 12, 31).

finance(1200).

s3306_c(alice_employer_s3306_b_15_pos,alice_s3306_b_15_pos,bob_s3306_b_15_pos,Day,Year) :-
    date_split(Day,Year,_,_),
    is_before(d2011_02_01,Day),
    is_before(Day,d2019_11_19).

purpose_(alice_employer_s3306_b_15_pos,"agricultural labor").
death_(bob_dies_s3306_b_15_pos).
agent_(bob_dies_s3306_b_15_pos,bob_s3306_b_15_pos).
start_(bob_dies_s3306_b_15_pos,d2019_11_25).
end_(bob_dies_s3306_b_15_pos,d2019_11_25).
marriage_(bob_and_charlie_s3306_b_15_pos).
agent_(bob_and_charlie_s3306_b_15_pos,bob_s3306_b_15_pos).
agent_(bob_and_charlie_s3306_b_15_pos,charlie_s3306_b_15_pos).
payment_(alice_pays_s3306_b_15_pos).
agent_(alice_pays_s3306_b_15_pos,alice_s3306_b_15_pos).
patient_(alice_pays_s3306_b_15_pos,charlie_s3306_b_15_pos).
start_(alice_pays_s3306_b_15_pos,d2020_01_20).
end_(alice_pays_s3306_b_15_pos,d2020_01_20).
purpose_(alice_pays_s3306_b_15_pos,alice_employer_s3306_b_15_pos).
amount_(alice_pays_s3306_b_15_pos,1200).

% Test
:- s3306_b_15(alice_pays_s3306_b_15_pos,alice_s3306_b_15_pos,charlie_s3306_b_15_pos,bob_s3306_b_15_pos,2020).
:- halt.
% Text
% Alice has paid $45252 to Bob for work done in the year 2017. In 2017, Alice has also paid $9832 into a retirement fund for Bob, and $5322 into health insurance for Charlie, who is Alice's father and has retired in 2016.

% Question
% Section 3306(b)(2)(A) applies to the payment Alice made to Bob for the year 2017. Contradiction

% Facts
person(alice_s3306_b_2_A_neg).
person(bob_s3306_b_2_A_neg).
person(charlie_s3306_b_2_A_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

finance(45252).
finance(9832).
finance(5322).

service_(alice_employer_s3306_b_2_A_neg).
patient_(alice_employer_s3306_b_2_A_neg,alice_s3306_b_2_A_neg).
agent_(alice_employer_s3306_b_2_A_neg,bob_s3306_b_2_A_neg).
start_(alice_employer_s3306_b_2_A_neg,d2017_01_01).
end_(alice_employer_s3306_b_2_A_neg,d2017_12_31).
payment_(alice_pays_bob_s3306_b_2_A_neg).
agent_(alice_pays_bob_s3306_b_2_A_neg,alice_s3306_b_2_A_neg).
patient_(alice_pays_bob_s3306_b_2_A_neg,bob_s3306_b_2_A_neg).
start_(alice_pays_bob_s3306_b_2_A_neg,d2017_01_01).
end_(alice_pays_bob_s3306_b_2_A_neg,d2017_12_31).
purpose_(alice_pays_bob_s3306_b_2_A_neg,alice_employer_s3306_b_2_A_neg).
amount_(alice_pays_bob_s3306_b_2_A_neg,45252).
payment_(alice_pays_retirement_s3306_b_2_A_neg).
agent_(alice_pays_retirement_s3306_b_2_A_neg,alice_s3306_b_2_A_neg).
patient_(alice_pays_retirement_s3306_b_2_A_neg,retirement_fund_s3306_b_2_A_neg).
purpose_(alice_pays_retirement_s3306_b_2_A_neg,"make provisions for employees in case of retirement").
plan_(retirement_fund_s3306_b_2_A_neg).
beneficiary_(alice_pays_retirement_s3306_b_2_A_neg,bob_s3306_b_2_A_neg).
start_(alice_pays_retirement_s3306_b_2_A_neg,d2017_01_01).
end_(alice_pays_retirement_s3306_b_2_A_neg,d2017_12_31).
amount_(alice_pays_retirement_s3306_b_2_A_neg,9832).
payment_(alice_pays_insurance_s3306_b_2_A_neg).
agent_(alice_pays_insurance_s3306_b_2_A_neg,alice_s3306_b_2_A_neg).
patient_(alice_pays_insurance_s3306_b_2_A_neg,health_insurance_fund_s3306_b_2_A_neg).
plan_(health_insurance_fund_s3306_b_2_A_neg).
purpose_(alice_pays_insurance_s3306_b_2_A_neg,"make provisions in case of sickness").
beneficiary_(alice_pays_insurance_s3306_b_2_A_neg,charlie_s3306_b_2_A_neg).
start_(alice_pays_insurance_s3306_b_2_A_neg,d2017_01_01).
end_(alice_pays_insurance_s3306_b_2_A_neg,d2017_12_31).
amount_(alice_pays_insurance_s3306_b_2_A_neg,5322).
father_(alice_and_charlie_s3306_b_2_A_neg).
agent_(alice_and_charlie_s3306_b_2_A_neg,charlie_s3306_b_2_A_neg).
patient_(alice_and_charlie_s3306_b_2_A_neg,alice_s3306_b_2_A_neg).
retirement_(charlie_retires_s3306_b_2_A_neg).
agent_(charlie_retires_s3306_b_2_A_neg,charlie_s3306_b_2_A_neg).
start_(charlie_retires_s3306_b_2_A_neg,d2016_01_01).

% Test
:- \+ s3306_b_2_A(alice_pays_bob_s3306_b_2_A_neg).
:- halt.
% Text
% Alice has paid $45252 to Bob for work done in the year 2017. In 2017, Alice has also paid $9832 into a retirement fund for Bob, and $5322 into health insurance for Bob.

% Question
% Section 3306(b)(2)(A) applies to the payment Alice made to the health insurance fund for the year 2017. Entailment

% Facts
person(alice_s3306_b_2_A_pos).
person(bob_s3306_b_2_A_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

finance(45252).
finance(9832).
finance(5322).

service_(alice_employer_s3306_b_2_A_pos).
patient_(alice_employer_s3306_b_2_A_pos,alice_s3306_b_2_A_pos).
agent_(alice_employer_s3306_b_2_A_pos,bob_s3306_b_2_A_pos).
start_(alice_employer_s3306_b_2_A_pos,d2017_01_01).
end_(alice_employer_s3306_b_2_A_pos,d2017_12_31).
payment_(alice_pays_bob_s3306_b_2_A_pos).
agent_(alice_pays_bob_s3306_b_2_A_pos,alice_s3306_b_2_A_pos).
patient_(alice_pays_bob_s3306_b_2_A_pos,bob_s3306_b_2_A_pos).
start_(alice_pays_bob_s3306_b_2_A_pos,d2017_01_01).
end_(alice_pays_bob_s3306_b_2_A_pos,d2017_12_31).
purpose_(alice_pays_bob_s3306_b_2_A_pos,alice_employer_s3306_b_2_A_pos).
amount_(alice_pays_bob_s3306_b_2_A_pos,45252).
payment_(alice_pays_retirement_s3306_b_2_A_pos).
agent_(alice_pays_retirement_s3306_b_2_A_pos,alice_s3306_b_2_A_pos).
patient_(alice_pays_retirement_s3306_b_2_A_pos,retirement_fund_s3306_b_2_A_pos).
plan_(retirement_fund_s3306_b_2_A_pos).
purpose_(retirement_fund_s3306_b_2_A_pos,"make provisions for employees in case of retirement").
beneficiary_(retirement_fund_s3306_b_2_A_pos,bob_s3306_b_2_A_pos).
start_(alice_pays_retirement_s3306_b_2_A_pos,d2017_01_01).
end_(alice_pays_retirement_s3306_b_2_A_pos,d2017_12_31).
amount_(alice_pays_retirement_s3306_b_2_A_pos,9832).
payment_(alice_pays_insurance_s3306_b_2_A_pos).
agent_(alice_pays_insurance_s3306_b_2_A_pos,alice_s3306_b_2_A_pos).
patient_(alice_pays_insurance_s3306_b_2_A_pos,health_insurance_fund_s3306_b_2_A_pos).
plan_(health_insurance_fund_s3306_b_2_A_pos).
purpose_(health_insurance_fund_s3306_b_2_A_pos,"make provisions for employees in case of sickness").
beneficiary_(health_insurance_fund_s3306_b_2_A_pos,bob_s3306_b_2_A_pos).
start_(alice_pays_insurance_s3306_b_2_A_pos,d2017_01_01).
end_(alice_pays_insurance_s3306_b_2_A_pos,d2017_12_31).
amount_(alice_pays_insurance_s3306_b_2_A_pos,5322).

% Test
:- s3306_b_2_A(health_insurance_fund_s3306_b_2_A_pos).
:- halt.
% Text
% Alice has been running a typewriter factory since February 1st, 2016. Bob is an employee at the typewriter factory. On October 2nd 2017, Alice has paid Bob $323 for painting her house.

% Question
% Section 3306(b)(7) applies to the payment Alice made to Bob. Contradiction

% Facts
person(alice_s3306_b_7_neg).
person(bob_s3306_b_7_neg).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_02_01).
date_split(d2016_02_01, 2016, 2, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_06_01).
date_split(d2017_06_01, 2017, 6, 1).
date(d2017_08_31).
date_split(d2017_08_31, 2017, 8, 31).
date(d2017_10_02).
date_split(d2017_10_02, 2017, 10, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

finance(323).
medium("cash").

business_(alice_runs_a_factory_s3306_b_7_neg).
agent_(alice_runs_a_factory_s3306_b_7_neg,alice_s3306_b_7_neg).
type_(alice_runs_a_factory_s3306_b_7_neg,"manufacturing").
start_(alice_runs_a_factory_s3306_b_7_neg,d2016_02_01).
service_(alice_employer_s3306_b_7_neg).
patient_(alice_employer_s3306_b_7_neg,alice_s3306_b_7_neg).
agent_(alice_employer_s3306_b_7_neg,bob_s3306_b_7_neg).
start_(alice_employer_s3306_b_7_neg,d2017_06_01).
end_(alice_employer_s3306_b_7_neg,d2017_08_31).
type_(alice_employer_s3306_b_7_neg,"painting Alice's house").
payment_(alice_pays_bob_s3306_b_7_neg).
agent_(alice_pays_bob_s3306_b_7_neg,alice_s3306_b_7_neg).
patient_(alice_pays_bob_s3306_b_7_neg,bob_s3306_b_7_neg).
start_(alice_pays_bob_s3306_b_7_neg,d2017_10_02).
end_(alice_pays_bob_s3306_b_7_neg,d2017_10_02).
purpose_(alice_pays_bob_s3306_b_7_neg,alice_employer_s3306_b_7_neg).
amount_(alice_pays_bob_s3306_b_7_neg,323).
means_(alice_pays_bob_s3306_b_7_neg,"cash").
s3306_c(alice_employer_s3306_b_7_neg,alice_s3306_b_7_neg,bob_s3306_b_7_neg,Day,2017) :-
    is_before(d2017_06_01,Day),
    is_before(Day,d2017_08_31).

% Test
:- \+ s3306_b_7(alice_pays_bob_s3306_b_7_neg,alice_employer_s3306_b_7_neg,alice_s3306_b_7_neg,bob_s3306_b_7_neg,"cash","manufacturing").
:- halt.
% Text
% Alice has been running a typewriter factory since February 1st, 2016. Bob is an employee at the typewriter factory. On October 2nd 2017, Alice has given a typewriter of value $323 to Bob in exchange for Bob painting Alice's house.

% Question
% Section 3306(b)(7) applies to the payment Alice made to Bob. Entailment

% Facts
person(alice_s3306_b_7_pos).
person(bob_s3306_b_7_pos).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_02_01).
date_split(d2016_02_01, 2016, 2, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_06_01).
date_split(d2017_06_01, 2017, 6, 1).
date(d2017_08_31).
date_split(d2017_08_31, 2017, 8, 31).
date(d2017_10_02).
date_split(d2017_10_02, 2017, 10, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

finance(323).
medium("goods").

business_(alice_runs_a_factory_s3306_b_7_pos).
agent_(alice_runs_a_factory_s3306_b_7_pos,alice_s3306_b_7_pos).
type_(alice_runs_a_factory_s3306_b_7_pos,"manufacturing").
start_(alice_runs_a_factory_s3306_b_7_pos,d2016_02_01).
service_(alice_employer_s3306_b_7_pos).
patient_(alice_employer_s3306_b_7_pos,alice_s3306_b_7_pos).
agent_(alice_employer_s3306_b_7_pos,bob_s3306_b_7_pos).
start_(alice_employer_s3306_b_7_pos,d2017_06_01).
end_(alice_employer_s3306_b_7_pos,d2017_08_31).
type_(alice_employer_s3306_b_7_pos,"painting Alice's house").
payment_(alice_pays_bob_s3306_b_7_pos).
agent_(alice_pays_bob_s3306_b_7_pos,alice_s3306_b_7_pos).
patient_(alice_pays_bob_s3306_b_7_pos,bob_s3306_b_7_pos).
start_(alice_pays_bob_s3306_b_7_pos,d2017_10_02).
end_(alice_pays_bob_s3306_b_7_pos,d2017_10_02).
purpose_(alice_pays_bob_s3306_b_7_pos,alice_employer_s3306_b_7_pos).
amount_(alice_pays_bob_s3306_b_7_pos,323).
means_(alice_pays_bob_s3306_b_7_pos,"goods").
s3306_c(alice_employer_s3306_b_7_pos,alice_s3306_b_7_pos,bob_s3306_b_7_pos,Day,2017) :-
    is_before(d2017_06_01,Day),
    is_before(Day,d2017_08_31).

% Test
:- s3306_b_7(alice_pays_bob_s3306_b_7_pos,alice_employer_s3306_b_7_pos,alice_s3306_b_7_pos,bob_s3306_b_7_pos,"goods","manufacturing").
:- halt.
% Text
% Over the year 2018, Alice has paid $2325 in hay to Bob for agricultural labor.

% Question
% Section 3306(b) applies to the hay paid by Alice to Bob for the year 2018. Contradiction

% Facts
person(alice_s3306_b_neg).
person(bob_s3306_b_neg).

year(2018).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

finance(2325).
medium("kind").

service_(alice_employer_s3306_b_neg).
patient_(alice_employer_s3306_b_neg,alice_s3306_b_neg).
agent_(alice_employer_s3306_b_neg,bob_s3306_b_neg).
start_(alice_employer_s3306_b_neg,d2018_01_01).
end_(alice_employer_s3306_b_neg,d2018_12_31).
purpose_(alice_employer_s3306_b_neg,"agricultural labor").
payment_(alice_pays_s3306_b_neg).
agent_(alice_pays_s3306_b_neg,alice_s3306_b_neg).
patient_(alice_pays_s3306_b_neg,bob_s3306_b_neg).
start_(alice_pays_s3306_b_neg,d2018_01_01).
end_(alice_pays_s3306_b_neg,d2018_12_31).
purpose_(alice_pays_s3306_b_neg,alice_employer_s3306_b_neg).
amount_(alice_pays_s3306_b_neg,2325).
means_(alice_pays_s3306_b_neg,"kind").

% Test
:- \+ s3306_b(2325,alice_pays_s3306_b_neg,alice_employer_s3306_b_neg,alice_s3306_b_neg,bob_s3306_b_neg,alice_s3306_b_neg,bob_s3306_b_neg,"kind").
:- halt.
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
medium("cash").

service_(alice_employer_s3306_b_pos).
patient_(alice_employer_s3306_b_pos,alice_s3306_b_pos).
agent_(alice_employer_s3306_b_pos,bob_s3306_b_pos).
start_(alice_employer_s3306_b_pos,d2018_01_01).
end_(alice_employer_s3306_b_pos,d2018_12_31).
purpose_(alice_employer_s3306_b_pos,"walking her dog").
payment_(alice_pays_s3306_b_pos).
agent_(alice_pays_s3306_b_pos,alice_s3306_b_pos).
patient_(alice_pays_s3306_b_pos,bob_s3306_b_pos).
start_(alice_pays_s3306_b_pos,d2018_01_01).
end_(alice_pays_s3306_b_pos,d2018_12_31).
purpose_(alice_pays_s3306_b_pos,alice_employer_s3306_b_pos).
amount_(alice_pays_s3306_b_pos,2325).
means_(alice_pays_s3306_b_pos,"cash").

% Test
:- s3306_b(2325,alice_pays_s3306_b_pos,alice_employer_s3306_b_pos,alice_s3306_b_pos,bob_s3306_b_pos,alice_s3306_b_pos,bob_s3306_b_pos,"cash").
:- halt.
% Text
% Alice was paid $3200 in 2017 for services performed for Johns Hopkins University. Alice was enrolled at Johns Hopkins University and attending classes from August 27, 2011 to May 29th, 2016.

% Question
% Section 3306(c)(10)(A)(i) applies to Alice's employment situation in 2017. Contradiction

% Facts
person(alice_s3306_c_10_A_i_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2011).
date(d2011_01_01).
date_split(d2011_01_01, 2011, 1, 1).
date(d2011_08_27).
date_split(d2011_08_27, 2011, 8, 27).
date(d2011_12_31).
date_split(d2011_12_31, 2011, 12, 31).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_05_29).
date_split(d2016_05_29, 2016, 5, 29).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

location_name(baltimore).
location_name(maryland).
location_name(usa).

finance(3200).

educational_institution_(hopkins_is_a_university_s3306_c_10_A_i_neg).
agent_(hopkins_is_a_university_s3306_c_10_A_i_neg,"johns hopkins university").
service_(alice_employed_s3306_c_10_A_i_neg).
patient_(alice_employed_s3306_c_10_A_i_neg,"johns hopkins university").
agent_(alice_employed_s3306_c_10_A_i_neg,alice_s3306_c_10_A_i_neg).
start_(alice_employed_s3306_c_10_A_i_neg,d2017_01_01).
end_(alice_employed_s3306_c_10_A_i_neg,d2017_12_31).
location_(alice_employed_s3306_c_10_A_i_neg,baltimore).
location_(alice_employed_s3306_c_10_A_i_neg,maryland).
location_(alice_employed_s3306_c_10_A_i_neg,usa).
payment_(alice_is_paid_s3306_c_10_A_i_neg).
agent_(alice_is_paid_s3306_c_10_A_i_neg,"johns hopkins university").
patient_(alice_is_paid_s3306_c_10_A_i_neg,alice_s3306_c_10_A_i_neg).
start_(alice_is_paid_s3306_c_10_A_i_neg,d2017_12_31).
purpose_(alice_is_paid_s3306_c_10_A_i_neg,alice_employed_s3306_c_10_A_i_neg).
amount_(alice_is_paid_s3306_c_10_A_i_neg,3200).
enrollment_(alice_goes_to_hopkins_s3306_c_10_A_i_neg).
agent_(alice_goes_to_hopkins_s3306_c_10_A_i_neg,alice_s3306_c_10_A_i_neg).
patient_(alice_goes_to_hopkins_s3306_c_10_A_i_neg,"johns hopkins university").
start_(alice_goes_to_hopkins_s3306_c_10_A_i_neg,d2011_08_27).
end_(alice_goes_to_hopkins_s3306_c_10_A_i_neg,d2016_05_29).
attending_classes_(alice_goes_to_class_s3306_c_10_A_i_neg).
agent_(alice_goes_to_class_s3306_c_10_A_i_neg,alice_s3306_c_10_A_i_neg).
location_(alice_goes_to_class_s3306_c_10_A_i_neg,"johns hopkins university").
start_(alice_goes_to_class_s3306_c_10_A_i_neg,d2011_08_27).
end_(alice_goes_to_class_s3306_c_10_A_i_neg,d2016_05_29).

% Test
:- \+ s3306_c_10_A_i(alice_s3306_c_10_A_i_neg,"johns hopkins university",d2017_01_01).
:- halt.
% Text
% Alice was paid $3200 in 2017 for services performed for Johns Hopkins University. Alice was enrolled at Johns Hopkins University and attending classes from August 29, 2015 to May 30th, 2019.

% Question
% Section 3306(c)(10)(A)(i) applies to Alice's employment situation in 2017. Entailment

% Facts
person(alice_s3306_c_10_A_i_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_08_29).
date_split(d2015_08_29, 2015, 8, 29).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_05_30).
date_split(d2019_05_30, 2019, 5, 30).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

location_name(baltimore).
location_name(maryland).
location_name(usa).
location_name("johns hopkins university").

finance(3200).

service_(alice_employed_s3306_c_10_A_i_pos).
patient_(alice_employed_s3306_c_10_A_i_pos,"johns hopkins university").
agent_(alice_employed_s3306_c_10_A_i_pos,alice_s3306_c_10_A_i_pos).
start_(alice_employed_s3306_c_10_A_i_pos,d2017_01_01).
end_(alice_employed_s3306_c_10_A_i_pos,d2017_12_31).
location_(alice_employed_s3306_c_10_A_i_pos,baltimore).
location_(alice_employed_s3306_c_10_A_i_pos,maryland).
location_(alice_employed_s3306_c_10_A_i_pos,usa).
payment_(alice_is_paid_s3306_c_10_A_i_pos).
agent_(alice_is_paid_s3306_c_10_A_i_pos,"johns hopkins university").
patient_(alice_is_paid_s3306_c_10_A_i_pos,alice_s3306_c_10_A_i_pos).
start_(alice_is_paid_s3306_c_10_A_i_pos,d2017_12_31).
purpose_(alice_is_paid_s3306_c_10_A_i_pos,alice_employed_s3306_c_10_A_i_pos).
amount_(alice_is_paid_s3306_c_10_A_i_pos,3200).
educational_institution_(hopkins_is_a_university_s3306_c_10_A_i_pos).
agent_(hopkins_is_a_university_s3306_c_10_A_i_pos,"johns hopkins university").
enrollment_(alice_goes_to_hopkins_s3306_c_10_A_i_pos).
agent_(alice_goes_to_hopkins_s3306_c_10_A_i_pos,alice_s3306_c_10_A_i_pos).
patient_(alice_goes_to_hopkins_s3306_c_10_A_i_pos,"johns hopkins university").
start_(alice_goes_to_hopkins_s3306_c_10_A_i_pos,d2015_08_29).
end_(alice_goes_to_hopkins_s3306_c_10_A_i_pos,d2019_05_30).
attending_classes_(alice_goes_to_class_s3306_c_10_A_i_pos).
agent_(alice_goes_to_class_s3306_c_10_A_i_pos,alice_s3306_c_10_A_i_pos).
location_(alice_goes_to_class_s3306_c_10_A_i_pos,"johns hopkins university").
start_(alice_goes_to_class_s3306_c_10_A_i_pos,d2015_08_29).
end_(alice_goes_to_class_s3306_c_10_A_i_pos,d2019_05_30).

% Test
:- s3306_c_10_A(alice_employed_s3306_c_10_A_i_pos,"johns hopkins university",alice_s3306_c_10_A_i_pos,d2017_01_01), s3306_c_10_A_i(alice_s3306_c_10_A_i_pos,"johns hopkins university",d2017_01_01).
:- halt.
% Text
% Alice's father, Bob, was paid $3200 in 2017 for services performed for Johns Hopkins University. Alice was enrolled at Johns Hopkins University and attending classes from August 29, 2015 to May 30th, 2019.

% Question
% Section 3306(c)(10)(A)(ii) applies to Bob's employment situation in 2017. Contradiction

% Facts
person(alice_s3306_c_10_A_ii_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_08_29).
date_split(d2015_08_29, 2015, 8, 29).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_05_30).
date_split(d2019_05_30, 2019, 5, 30).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

location_name(baltimore).
location_name(maryland).
location_name(usa).
location_name("johns hopkins university").

finance(3200).

educational_institution_(hopkins_is_a_university_s3306_c_10_A_ii_neg).
agent_(hopkins_is_a_university_s3306_c_10_A_ii_neg,"johns hopkins university").
father_(bob_and_alice_s3306_c_10_A_ii_neg).
agent_(bob_and_alice_s3306_c_10_A_ii_neg,bob_s3306_c_10_A_ii_neg).
patient_(bob_and_alice_s3306_c_10_A_ii_neg,alice_s3306_c_10_A_ii_neg).
service_(bob_employed_s3306_c_10_A_ii_neg).
patient_(bob_employed_s3306_c_10_A_ii_neg,"johns hopkins university").
agent_(bob_employed_s3306_c_10_A_ii_neg,bob_s3306_c_10_A_ii_neg).
start_(bob_employed_s3306_c_10_A_ii_neg,d2017_01_01).
end_(bob_employed_s3306_c_10_A_ii_neg,d2017_12_31).
location_(bob_employed_s3306_c_10_A_ii_neg,baltimore).
location_(bob_employed_s3306_c_10_A_ii_neg,maryland).
location_(bob_employed_s3306_c_10_A_ii_neg,usa).
payment_(bob_is_paid_s3306_c_10_A_ii_neg).
agent_(bob_is_paid_s3306_c_10_A_ii_neg,"johns hopkins university").
patient_(bob_is_paid_s3306_c_10_A_ii_neg,bob_s3306_c_10_A_ii_neg).
start_(bob_is_paid_s3306_c_10_A_ii_neg,d2017_12_31).
purpose_(bob_is_paid_s3306_c_10_A_ii_neg,bob_employed_s3306_c_10_A_ii_neg).
amount_(bob_is_paid_s3306_c_10_A_ii_neg,3200).
enrollment_(alice_goes_to_hopkins_s3306_c_10_A_ii_neg).
agent_(alice_goes_to_hopkins_s3306_c_10_A_ii_neg,alice_s3306_c_10_A_ii_neg).
patient_(alice_goes_to_hopkins_s3306_c_10_A_ii_neg,"johns hopkins university").
start_(alice_goes_to_hopkins_s3306_c_10_A_ii_neg,d2015_08_29).
end_(alice_goes_to_hopkins_s3306_c_10_A_ii_neg,d2019_05_30).
attending_classes_(alice_goes_to_class_s3306_c_10_A_ii_neg).
agent_(alice_goes_to_class_s3306_c_10_A_ii_neg,alice_s3306_c_10_A_ii_neg).
location_(alice_goes_to_class_s3306_c_10_A_ii_neg,"johns hopkins university").
start_(alice_goes_to_class_s3306_c_10_A_ii_neg,d2015_08_29).
end_(alice_goes_to_class_s3306_c_10_A_ii_neg,d2019_05_30).

% Test
:- \+ s3306_c_10_A_ii(alice_s3306_c_10_A_ii_neg,bob_s3306_c_10_A_ii_neg,d2017_01_01).
:- halt.
% Text
% Alice's husband, Bob, was paid $3200 in 2017 for services performed for Johns Hopkins University. Alice was enrolled at Johns Hopkins University and attending classes from August 29, 2015 to May 30th, 2019.

% Question
% Section 3306(c)(10)(A)(ii) applies to Bob's employment situation in 2017. Entailment

% Facts
person(alice_s3306_c_10_A_ii_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_08_29).
date_split(d2015_08_29, 2015, 8, 29).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_05_30).
date_split(d2019_05_30, 2019, 5, 30).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

location_name(baltimore).
location_name(maryland).
location_name(usa).
location_name("johns hopkins university").

finance(3200).

educational_institution_(hopkins_is_a_university_s3306_c_10_A_ii_pos).
agent_(hopkins_is_a_university_s3306_c_10_A_ii_pos,"johns hopkins university").
marriage_(bob_and_alice_s3306_c_10_A_ii_pos).
agent_(bob_and_alice_s3306_c_10_A_ii_pos,bob_s3306_c_10_A_ii_pos).
agent_(bob_and_alice_s3306_c_10_A_ii_pos,alice_s3306_c_10_A_ii_pos).
service_(bob_employed_s3306_c_10_A_ii_pos).
patient_(bob_employed_s3306_c_10_A_ii_pos,"johns hopkins university").
agent_(bob_employed_s3306_c_10_A_ii_pos,bob_s3306_c_10_A_ii_pos).
start_(bob_employed_s3306_c_10_A_ii_pos,d2017_01_01).
end_(bob_employed_s3306_c_10_A_ii_pos,d2017_12_31).
location_(bob_employed_s3306_c_10_A_ii_pos,baltimore).
location_(bob_employed_s3306_c_10_A_ii_pos,maryland).
location_(bob_employed_s3306_c_10_A_ii_pos,usa).
payment_(bob_is_paid_s3306_c_10_A_ii_pos).
agent_(bob_is_paid_s3306_c_10_A_ii_pos,"johns hopkins university").
patient_(bob_is_paid_s3306_c_10_A_ii_pos,bob_s3306_c_10_A_ii_pos).
start_(bob_is_paid_s3306_c_10_A_ii_pos,d2017_12_31).
purpose_(bob_is_paid_s3306_c_10_A_ii_pos,bob_employed_s3306_c_10_A_ii_pos).
amount_(bob_is_paid_s3306_c_10_A_ii_pos,3200).
enrollment_(alice_goes_to_hopkins_s3306_c_10_A_ii_pos).
agent_(alice_goes_to_hopkins_s3306_c_10_A_ii_pos,alice_s3306_c_10_A_ii_pos).
patient_(alice_goes_to_hopkins_s3306_c_10_A_ii_pos,"johns hopkins university").
start_(alice_goes_to_hopkins_s3306_c_10_A_ii_pos,d2015_08_29).
end_(alice_goes_to_hopkins_s3306_c_10_A_ii_pos,d2019_05_30).
attending_classes_(alice_goes_to_class_s3306_c_10_A_ii_pos).
agent_(alice_goes_to_class_s3306_c_10_A_ii_pos,alice_s3306_c_10_A_ii_pos).
location_(alice_goes_to_class_s3306_c_10_A_ii_pos,"johns hopkins university").
start_(alice_goes_to_class_s3306_c_10_A_ii_pos,d2015_08_29).
end_(alice_goes_to_class_s3306_c_10_A_ii_pos,d2019_05_30).

% Test
:- s3306_c_10_A_ii(alice_s3306_c_10_A_ii_pos,bob_s3306_c_10_A_ii_pos,d2017_01_01).
:- halt.
% Text
% Alice was paid $3200 in 2017 for services performed for Johns Hopkins University. Alice was enrolled as a physics major at Johns Hopkins University and attending classes from August 29, 2015 to May 30th, 2019.

% Question
% Section 3306(c)(13) applies to Alice's employment situation in 2017. Contradiction

% Facts
person(alice_s3306_c_13_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_08_29).
date_split(d2015_08_29, 2015, 8, 29).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_05_30).
date_split(d2019_05_30, 2019, 5, 30).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

location_name(baltimore).
location_name(maryland).
location_name(usa).
location_name("johns hopkins university").

finance(3200).

service_(alice_employed_s3306_c_13_neg).
patient_(alice_employed_s3306_c_13_neg,"johns hopkins university").
agent_(alice_employed_s3306_c_13_neg,alice_s3306_c_13_neg).
start_(alice_employed_s3306_c_13_neg,d2017_01_01).
end_(alice_employed_s3306_c_13_neg,d2017_12_31).
location_(alice_employed_s3306_c_13_neg,baltimore).
location_(alice_employed_s3306_c_13_neg,maryland).
location_(alice_employed_s3306_c_13_neg,usa).
payment_(alice_is_paid_s3306_c_13_neg).
agent_(alice_is_paid_s3306_c_13_neg,"johns hopkins university").
patient_(alice_is_paid_s3306_c_13_neg,alice_s3306_c_13_neg).
start_(alice_is_paid_s3306_c_13_neg,d2017_12_31).
purpose_(alice_is_paid_s3306_c_13_neg,alice_employed_s3306_c_13_neg).
amount_(alice_is_paid_s3306_c_13_neg,3200).
educational_institution_(hopkins_is_a_university_s3306_c_13_neg).
agent_(hopkins_is_a_university_s3306_c_13_neg,"johns hopkins university").
enrollment_(alice_goes_to_hopkins_s3306_c_13_neg).
agent_(alice_goes_to_hopkins_s3306_c_13_neg,alice_s3306_c_13_neg).
patient_(alice_goes_to_hopkins_s3306_c_13_neg,"johns hopkins university").
start_(alice_goes_to_hopkins_s3306_c_13_neg,d2015_08_29).
end_(alice_goes_to_hopkins_s3306_c_13_neg,d2019_05_30).
attending_classes_(alice_goes_to_class_s3306_c_13_neg).
agent_(alice_goes_to_class_s3306_c_13_neg,alice_s3306_c_13_neg).
location_(alice_goes_to_class_s3306_c_13_neg,"johns hopkins university").
start_(alice_goes_to_class_s3306_c_13_neg,d2015_08_29).
end_(alice_goes_to_class_s3306_c_13_neg,d2019_05_30).

% Test
:- \+ s3306_c_13(alice_employed_s3306_c_13_neg,"johns hopkins university",alice_s3306_c_13_neg,d2017_01_01).
:- halt.
% Text
% Alice was paid $3200 in 2017 for services performed for Johns Hopkins School of Nursing. Alice was enrolled at Johns Hopkins School of Nursing and attending classes from August 29, 2015 to May 30th, 2019.

% Question
% Section 3306(c)(13) applies to Alice's employment situation in 2017. Entailment

% Facts
person(alice_s3306_c_13_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_08_29).
date_split(d2015_08_29, 2015, 8, 29).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_05_30).
date_split(d2019_05_30, 2019, 5, 30).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

location_name(baltimore).
location_name(maryland).
location_name(usa).
location_name("johns hopkins school of nursing").

finance(3200).

service_(alice_employed_s3306_c_13_pos).
patient_(alice_employed_s3306_c_13_pos,"johns hopkins school of nursing").
agent_(alice_employed_s3306_c_13_pos,alice_s3306_c_13_pos).
start_(alice_employed_s3306_c_13_pos,d2017_01_01).
end_(alice_employed_s3306_c_13_pos,d2017_12_31).
location_(alice_employed_s3306_c_13_pos,baltimore).
location_(alice_employed_s3306_c_13_pos,maryland).
location_(alice_employed_s3306_c_13_pos,usa).
payment_(alice_is_paid_s3306_c_13_pos).
agent_(alice_is_paid_s3306_c_13_pos,"johns hopkins school of nursing").
patient_(alice_is_paid_s3306_c_13_pos,alice_s3306_c_13_pos).
start_(alice_is_paid_s3306_c_13_pos,d2017_12_31).
purpose_(alice_is_paid_s3306_c_13_pos,alice_employed_s3306_c_13_pos).
amount_(alice_is_paid_s3306_c_13_pos,3200).
nurses_training_school_(hopkins_is_a_nursing_school_s3306_c_13_pos).
agent_(hopkins_is_a_nursing_school_s3306_c_13_pos,"johns hopkins school of nursing").
enrollment_(alice_goes_to_hopkins_s3306_c_13_pos).
agent_(alice_goes_to_hopkins_s3306_c_13_pos,alice_s3306_c_13_pos).
patient_(alice_goes_to_hopkins_s3306_c_13_pos,"johns hopkins school of nursing").
start_(alice_goes_to_hopkins_s3306_c_13_pos,d2015_08_29).
end_(alice_goes_to_hopkins_s3306_c_13_pos,d2019_05_30).
attending_classes_(alice_goes_to_class_s3306_c_13_pos).
agent_(alice_goes_to_class_s3306_c_13_pos,alice_s3306_c_13_pos).
location_(alice_goes_to_class_s3306_c_13_pos,"johns hopkins school of nursing").
start_(alice_goes_to_class_s3306_c_13_pos,d2015_08_29).
end_(alice_goes_to_class_s3306_c_13_pos,d2019_05_30).

% Test
:- s3306_c_13(alice_employed_s3306_c_13_pos,"johns hopkins school of nursing",alice_s3306_c_13_pos,d2017_01_01).
:- halt.
% Text
% Alice has paid $2300 to Bob for agricultural labor done from Feb 1st, 2017 to Sep 2nd, 2017, in Caracas, Venezuela. Alice and Bob are both American citizens.

% Question
% Section 3306(c)(1)(A)(i) applies to Alice employing Bob for the year 2017. Contradiction

% Facts
person(alice_s3306_c_1_A_i_neg).
person(bob_s3306_c_1_A_i_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

location_name("caracas, venezuela").
country_name("venezuela").

finance(2300).

service_(alice_employer_s3306_c_1_A_i_neg).
patient_(alice_employer_s3306_c_1_A_i_neg,alice_s3306_c_1_A_i_neg).
agent_(alice_employer_s3306_c_1_A_i_neg,bob_s3306_c_1_A_i_neg).
start_(alice_employer_s3306_c_1_A_i_neg,d2017_02_01).
end_(alice_employer_s3306_c_1_A_i_neg,d2017_09_02).
location_(alice_employer_s3306_c_1_A_i_neg,"caracas, venezuela").
country_("caracas, venezuela", "venezuela").
purpose_(alice_employer_s3306_c_1_A_i_neg,"agricultural labor").
payment_(alice_pays_s3306_c_1_A_i_neg).
agent_(alice_pays_s3306_c_1_A_i_neg,alice_s3306_c_1_A_i_neg).
patient_(alice_pays_s3306_c_1_A_i_neg,bob_s3306_c_1_A_i_neg).
start_(alice_pays_s3306_c_1_A_i_neg,d2017_09_02).
purpose_(alice_pays_s3306_c_1_A_i_neg,alice_employer_s3306_c_1_A_i_neg).
amount_(alice_pays_s3306_c_1_A_i_neg,2300).
citizenship_(alice_is_american_s3306_c_1_A_i_neg).
agent_(alice_is_american_s3306_c_1_A_i_neg,alice_s3306_c_1_A_i_neg).
patient_(alice_is_american_s3306_c_1_A_i_neg,"usa").
citizenship_(bob_is_american_s3306_c_1_A_i_neg).
agent_(bob_is_american_s3306_c_1_A_i_neg,bob_s3306_c_1_A_i_neg).
patient_(bob_is_american_s3306_c_1_A_i_neg,"usa").

% Test
:- \+ s3306_c_1_A_i(alice_s3306_c_1_A_i_neg,2300,bob_s3306_c_1_A_i_neg,alice_employer_s3306_c_1_A_i_neg,2017).
:- halt.
% Text
% Alice has paid $23200 in remuneration to Bob for agricultural labor done from Feb 1st, 2017 to Sep 2nd, 2017, in Caracas, Venezuela. Alice is an American employer.

% Question
% Section 3306(c)(1)(A)(i) applies to Alice employing Bob for the year 2017. Entailment

% Facts
person(alice_s3306_c_1_A_i_pos).
person(bob_s3306_c_1_A_i_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

location_name("caracas, venezuela").
country_name("venezuela").

finance(23200).

service_(alice_employer_s3306_c_1_A_i_pos).
patient_(alice_employer_s3306_c_1_A_i_pos,alice_s3306_c_1_A_i_pos).
agent_(alice_employer_s3306_c_1_A_i_pos,bob_s3306_c_1_A_i_pos).
start_(alice_employer_s3306_c_1_A_i_pos,d2017_02_01).
end_(alice_employer_s3306_c_1_A_i_pos,d2017_09_02).
location_(alice_employer_s3306_c_1_A_i_pos,"caracas, venezuela").
country_("caracas, venezuela", "venezuela").
purpose_(alice_employer_s3306_c_1_A_i_pos,"agricultural labor").
payment_(alice_pays_s3306_c_1_A_i_pos).
agent_(alice_pays_s3306_c_1_A_i_pos,alice_s3306_c_1_A_i_pos).
patient_(alice_pays_s3306_c_1_A_i_pos,bob_s3306_c_1_A_i_pos).
start_(alice_pays_s3306_c_1_A_i_pos,d2017_09_02).
purpose_(alice_pays_s3306_c_1_A_i_pos,alice_employer_s3306_c_1_A_i_pos).
amount_(alice_pays_s3306_c_1_A_i_pos,23200).
american_employer_(alice_is_american_employer_s3306_c_1_A_i_pos).
agent_(alice_is_american_employer_s3306_c_1_A_i_pos,alice_s3306_c_1_A_i_pos).
citizenship_(bob_is_american_s3306_c_1_A_i_pos).
agent_(bob_is_american_s3306_c_1_A_i_pos,bob_s3306_c_1_A_i_pos).
patient_(bob_is_american_s3306_c_1_A_i_pos,"usa").

% Test
:- s3306_c_1_A_i(alice_s3306_c_1_A_i_pos,23200,bob_s3306_c_1_A_i_pos,alice_employer_s3306_c_1_A_i_pos,2017).
:- halt.
% Text
% Alice has paid $3200 to Bob for domestic service done from Feb 1st, 2017 to Sep 2nd, 2017, in Caracas, Venezuela. Alice is an American employer.

% Question
% Section 3306(c)(1) applies to Alice employing Bob for the year 2017. Contradiction

% Facts
person(alice_s3306_c_1_neg).
person(bob_s3306_c_1_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

location_name("caracas, venezuela").
country_name("venezuela").

finance(3200).

service_(alice_employer_s3306_c_1_neg).
patient_(alice_employer_s3306_c_1_neg,alice_s3306_c_1_neg).
agent_(alice_employer_s3306_c_1_neg,bob_s3306_c_1_neg).
start_(alice_employer_s3306_c_1_neg,d2017_02_01).
end_(alice_employer_s3306_c_1_neg,d2017_09_02).
location_(alice_employer_s3306_c_1_neg,"caracas, venezuela").
country_("caracas, venezuela", "venezuela").
purpose_(alice_employer_s3306_c_1_neg,"domestic service").
payment_(alice_pays_s3306_c_1_neg).
agent_(alice_pays_s3306_c_1_neg,alice_s3306_c_1_neg).
patient_(alice_pays_s3306_c_1_neg,bob_s3306_c_1_neg).
start_(alice_pays_s3306_c_1_neg,d2017_09_02).
purpose_(alice_pays_s3306_c_1_neg,alice_employer_s3306_c_1_neg).
amount_(alice_pays_s3306_c_1_neg,3200).
american_employer_(alice_is_american_employer_s3306_c_1_neg).
agent_(alice_is_american_employer_s3306_c_1_neg,alice_s3306_c_1_neg).
citizenship_(bob_is_american_s3306_c_1_neg).
agent_(bob_is_american_s3306_c_1_neg,bob_s3306_c_1_neg).
patient_(bob_is_american_s3306_c_1_neg,"usa").

% Test
:- \+ s3306_c_1(alice_employer_s3306_c_1_neg,2017).
:- halt.
% Text
% Alice has paid $3200 to Bob for agricultural labor done from Feb 1st, 2017 to Sep 2nd, 2017, in Caracas, Venezuela. Alice is an American employer.

% Question
% Section 3306(c)(1) applies to Alice employing Bob for the year 2017. Entailment

% Facts
person(alice_s3306_c_1_pos).
person(bob_s3306_c_1_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

location_name("caracas, venezuela").
country_name("venezuela").

finance(3200).

service_(alice_employer_s3306_c_1_pos).
patient_(alice_employer_s3306_c_1_pos,alice_s3306_c_1_pos).
agent_(alice_employer_s3306_c_1_pos,bob_s3306_c_1_pos).
start_(alice_employer_s3306_c_1_pos,d2017_02_01).
end_(alice_employer_s3306_c_1_pos,d2017_09_02).
location_(alice_employer_s3306_c_1_pos,"caracas, venezuela").
country_("caracas, venezuela", "venezuela").
purpose_(alice_employer_s3306_c_1_pos,"agricultural labor").
payment_(alice_pays_s3306_c_1_pos).
agent_(alice_pays_s3306_c_1_pos,alice_s3306_c_1_pos).
patient_(alice_pays_s3306_c_1_pos,bob_s3306_c_1_pos).
start_(alice_pays_s3306_c_1_pos,d2017_09_02).
purpose_(alice_pays_s3306_c_1_pos,alice_employer_s3306_c_1_pos).
amount_(alice_pays_s3306_c_1_pos,3200).
american_employer_(alice_is_american_employer_s3306_c_1_pos).
agent_(alice_is_american_employer_s3306_c_1_pos,alice_s3306_c_1_pos).
citizenship_(bob_is_american_s3306_c_1_pos).
agent_(bob_is_american_s3306_c_1_pos,bob_s3306_c_1_pos).
patient_(bob_is_american_s3306_c_1_pos,"usa").

% Test
:- s3306_c_1(alice_employer_s3306_c_1_pos,2017).
:- halt.
% Text
% Alice was paid $200 in 2017 for services performed in a hospital. Alice was committed to a psychiatric hospital from January 24, 2015 to May 5th, 2019.

% Question
% Section 3306(c)(21) applies to Alice's employment situation in 2017. Contradiction

% Facts
person(alice_s3306_c_21_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_01_24).
date_split(d2015_01_24, 2015, 1, 24).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_05_05).
date_split(d2019_05_05, 2019, 5, 5).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

finance(200).

service_(alice_employed_s3306_c_21_neg).
patient_(alice_employed_s3306_c_21_neg,hospital_s3306_c_21_neg).
agent_(alice_employed_s3306_c_21_neg,alice_s3306_c_21_neg).
start_(alice_employed_s3306_c_21_neg,d2017_01_01).
end_(alice_employed_s3306_c_21_neg,d2017_12_31).
payment_(alice_is_paid_s3306_c_21_neg).
agent_(alice_is_paid_s3306_c_21_neg,hospital_s3306_c_21_neg).
patient_(alice_is_paid_s3306_c_21_neg,alice_s3306_c_21_neg).
start_(alice_is_paid_s3306_c_21_neg,d2017_12_31).
purpose_(alice_is_paid_s3306_c_21_neg,alice_employed_s3306_c_21_neg).
amount_(alice_is_paid_s3306_c_21_neg,200).
medical_institution_(hospital_is_a_medical_institution_s3306_c_21_neg).
agent_(hospital_is_a_medical_institution_s3306_c_21_neg,hospital_s3306_c_21_neg).
incarceration_(alice_goes_to_hospital_s3306_c_21_neg).
agent_(alice_goes_to_hospital_s3306_c_21_neg,alice_s3306_c_21_neg).
patient_(alice_goes_to_hospital_s3306_c_21_neg,hospital_s3306_c_21_neg).
start_(alice_goes_to_hospital_s3306_c_21_neg,d2015_01_24).
end_(alice_goes_to_hospital_s3306_c_21_neg,d2019_05_05).

% Test
:- \+ s3306_c_21(alice_employed_s3306_c_21_neg,alice_s3306_c_21_neg,hospital_s3306_c_21_neg,d2017_01_01).
:- halt.
% Text
% Alice was paid $200 in 2017 for services performed in jail. Alice was committed to jail from January 24, 2015 to May 5th, 2019.

% Question
% Section 3306(c)(21) applies to Alice's employment situation in 2017. Entailment

% Facts
person(alice_s3306_c_21_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2015).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_01_24).
date_split(d2015_01_24, 2015, 1, 24).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_05_05).
date_split(d2019_05_05, 2019, 5, 5).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

finance(200).

service_(alice_employed_s3306_c_21_pos).
patient_(alice_employed_s3306_c_21_pos,jail_s3306_c_21_pos).
agent_(alice_employed_s3306_c_21_pos,alice_s3306_c_21_pos).
start_(alice_employed_s3306_c_21_pos,d2017_01_01).
end_(alice_employed_s3306_c_21_pos,d2017_12_31).
payment_(alice_is_paid_s3306_c_21_pos).
agent_(alice_is_paid_s3306_c_21_pos,jail_s3306_c_21_pos).
patient_(alice_is_paid_s3306_c_21_pos,alice_s3306_c_21_pos).
start_(alice_is_paid_s3306_c_21_pos,d2017_12_31).
purpose_(alice_is_paid_s3306_c_21_pos,alice_employed_s3306_c_21_pos).
amount_(alice_is_paid_s3306_c_21_pos,200).
penal_institution_(jail_is_a_penal_institution_s3306_c_21_pos).
agent_(jail_is_a_penal_institution_s3306_c_21_pos,jail_s3306_c_21_pos).
incarceration_(alice_goes_to_jail_s3306_c_21_pos).
agent_(alice_goes_to_jail_s3306_c_21_pos,alice_s3306_c_21_pos).
patient_(alice_goes_to_jail_s3306_c_21_pos,jail_s3306_c_21_pos).
start_(alice_goes_to_jail_s3306_c_21_pos,d2015_01_24).
end_(alice_goes_to_jail_s3306_c_21_pos,d2019_05_05).

% Test
:- s3306_c_21(alice_employed_s3306_c_21_pos,alice_s3306_c_21_pos,jail_s3306_c_21_pos,d2017_01_01).
:- halt.
% Text
% Alice has paid wages of $3200 to Bob for domestic service done in her home from Feb 1st, 2017 to Sep 2nd, 2017, in Baltimore, Maryland, USA.

% Question
% Section 3306(c)(2) applies to Alice employing Bob for the year 2017. Contradiction

% Facts
person(alice_s3306_c_2_neg).
person(bob_s3306_c_2_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

location_name(baltimore).
location_name(maryland).
location_name(usa).
location_name("private home_s3306_c_2_neg").

finance(3200).

service_(alice_employer_s3306_c_2_neg).
patient_(alice_employer_s3306_c_2_neg,alice_s3306_c_2_neg).
agent_(alice_employer_s3306_c_2_neg,bob_s3306_c_2_neg).
start_(alice_employer_s3306_c_2_neg,d2017_02_01).
end_(alice_employer_s3306_c_2_neg,d2017_09_02).
location_(alice_employer_s3306_c_2_neg,baltimore).
location_(alice_employer_s3306_c_2_neg,maryland).
location_(alice_employer_s3306_c_2_neg,usa).
purpose_(alice_employer_s3306_c_2_neg,"domestic service").
location_(alice_employer_s3306_c_2_neg,"private home_s3306_c_2_neg").
payment_(alice_pays_s3306_c_2_neg).
agent_(alice_pays_s3306_c_2_neg,alice_s3306_c_2_neg).
patient_(alice_pays_s3306_c_2_neg,bob_s3306_c_2_neg).
start_(alice_pays_s3306_c_2_neg,d2017_09_02).
purpose_(alice_pays_s3306_c_2_neg,alice_employer_s3306_c_2_neg).
amount_(alice_pays_s3306_c_2_neg,3200).
s3306_b(3200,alice_pays_s3306_c_2_neg,alice_employer_s3306_c_2_neg,alice_s3306_c_2_neg,bob_s3306_c_2_neg,alice_s3306_c_2_neg,bob_s3306_c_2_neg,"cash").

% Test
:- \+ s3306_c_2(alice_employer_s3306_c_2_neg,baltimore,2017).
:- \+ s3306_c_2(alice_employer_s3306_c_2_neg,maryland,2017).
:- \+ s3306_c_2(alice_employer_s3306_c_2_neg,usa,2017).
:- \+ s3306_c_2(alice_employer_s3306_c_2_neg,"private home_s3306_c_2_neg",2017).
:- halt.
% Text
% Alice has paid wages of $300 to Bob for domestic service done from Feb 1st, 2017 to Sep 2nd, 2017, in Baltimore, Maryland, USA.

% Question
% Section 3306(c)(2) applies to Alice employing Bob for the year 2017. Entailment

% Facts
person(alice_s3306_c_2_pos).
person(bob_s3306_c_2_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

location_name(baltimore).
location_name(maryland).
location_name(usa).
location_name("private home_s3306_c_2_pos").

finance(300).

service_(alice_employer_s3306_c_2_pos).
patient_(alice_employer_s3306_c_2_pos,alice_s3306_c_2_pos).
agent_(alice_employer_s3306_c_2_pos,bob_s3306_c_2_pos).
start_(alice_employer_s3306_c_2_pos,d2017_02_01).
end_(alice_employer_s3306_c_2_pos,d2017_09_02).
location_(alice_employer_s3306_c_2_pos,baltimore).
location_(alice_employer_s3306_c_2_pos,maryland).
location_(alice_employer_s3306_c_2_pos,usa).
purpose_(alice_employer_s3306_c_2_pos,"domestic service").
location_(alice_employer_s3306_c_2_pos,"private home_s3306_c_2_pos").
payment_(alice_pays_s3306_c_2_pos).
agent_(alice_pays_s3306_c_2_pos,alice_s3306_c_2_pos).
patient_(alice_pays_s3306_c_2_pos,bob_s3306_c_2_pos).
start_(alice_pays_s3306_c_2_pos,d2017_09_02).
purpose_(alice_pays_s3306_c_2_pos,alice_employer_s3306_c_2_pos).
amount_(alice_pays_s3306_c_2_pos,300).
s3306_b(300,alice_pays_s3306_c_2_pos,alice_employer_s3306_c_2_pos,alice_s3306_c_2_pos,bob_s3306_c_2_pos,alice_s3306_c_2_pos,bob_s3306_c_2_pos,"cash").

% Test
% :- s3306_c_2(alice_employer_s3306_c_2_pos,_,2017).
:- s3306_c_2(alice_employer_s3306_c_2_pos,baltimore,2017).
:- s3306_c_2(alice_employer_s3306_c_2_pos,maryland,2017).
:- s3306_c_2(alice_employer_s3306_c_2_pos,usa,2017).
:- s3306_c_2(alice_employer_s3306_c_2_pos,"private home_s3306_c_2_pos",2017).
:- halt.
% Text
% Alice has paid $3200 to her brother Bob for work done from Feb 1st, 2017 to Sep 2nd, 2017, in Baltimore, Maryland, USA.

% Question
% Section 3306(c)(5) applies to Alice employing Bob for the year 2017. Contradiction

% Facts
person(alice_s3306_c_5_neg).
person(bob_s3306_c_5_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

location_name(baltimore).
location_name(maryland).
location_name(usa).

finance(3200).

service_(alice_employer_s3306_c_5_neg).
patient_(alice_employer_s3306_c_5_neg,alice_s3306_c_5_neg).
agent_(alice_employer_s3306_c_5_neg,bob_s3306_c_5_neg).
start_(alice_employer_s3306_c_5_neg,d2017_02_01).
end_(alice_employer_s3306_c_5_neg,d2017_09_02).
location_(alice_employer_s3306_c_5_neg,baltimore).
location_(alice_employer_s3306_c_5_neg,maryland).
location_(alice_employer_s3306_c_5_neg,usa).
payment_(alice_pays_s3306_c_5_neg).
agent_(alice_pays_s3306_c_5_neg,alice_s3306_c_5_neg).
patient_(alice_pays_s3306_c_5_neg,bob_s3306_c_5_neg).
start_(alice_pays_s3306_c_5_neg,d2017_09_02).
purpose_(alice_pays_s3306_c_5_neg,alice_employer_s3306_c_5_neg).
amount_(alice_pays_s3306_c_5_neg,3200).
sibling_(bob_brother_of_alice_s3306_c_5_neg).
agent_(bob_brother_of_alice_s3306_c_5_neg,bob_s3306_c_5_neg).
patient_(bob_brother_of_alice_s3306_c_5_neg,alice_s3306_c_5_neg).

% Test
:- \+ s3306_c_5(alice_employer_s3306_c_5_neg,alice_s3306_c_5_neg,bob_s3306_c_5_neg,d2017_02_01).
:- halt.
% Text
% Alice has paid $3200 to her father Bob for work done from Feb 1st, 2017 to Sep 2nd, 2017, in Baltimore, Maryland, USA.

% Question
% Section 3306(c)(5) applies to Alice employing Bob for the year 2017. Entailment

% Facts
person(alice_s3306_c_5_pos).
person(bob_s3306_c_5_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

location_name(baltimore).
location_name(maryland).
location_name(usa).

finance(3200).

service_(alice_employer_s3306_c_5_pos).
patient_(alice_employer_s3306_c_5_pos,alice_s3306_c_5_pos).
agent_(alice_employer_s3306_c_5_pos,bob_s3306_c_5_pos).
start_(alice_employer_s3306_c_5_pos,d2017_02_01).
end_(alice_employer_s3306_c_5_pos,d2017_09_02).
location_(alice_employer_s3306_c_5_pos,baltimore).
location_(alice_employer_s3306_c_5_pos,maryland).
location_(alice_employer_s3306_c_5_pos,usa).
payment_(alice_pays_s3306_c_5_pos).
agent_(alice_pays_s3306_c_5_pos,alice_s3306_c_5_pos).
patient_(alice_pays_s3306_c_5_pos,bob_s3306_c_5_pos).
start_(alice_pays_s3306_c_5_pos,d2017_09_02).
purpose_(alice_pays_s3306_c_5_pos,alice_employer_s3306_c_5_pos).
amount_(alice_pays_s3306_c_5_pos,3200).
father_(bob_father_of_alice_s3306_c_5_pos).
agent_(bob_father_of_alice_s3306_c_5_pos,bob_s3306_c_5_pos).
patient_(bob_father_of_alice_s3306_c_5_pos,alice_s3306_c_5_pos).

% Test
:- s3306_c_5(alice_employer_s3306_c_5_pos,alice_s3306_c_5_pos,bob_s3306_c_5_pos,d2017_02_01).
:- halt.
% Text
% Alice has paid $3200 to Bob for work done from Feb 1st, 2017 to Sep 2nd, 2017, in Toronto, Ontario, Canada.

% Question
% Section 3306(c)(A) applies to Alice employing Bob for the year 2017. Contradiction

% Facts
person(alice_s3306_c_A_neg).
person(bob_s3306_c_A_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

location_name("toronto, ontario, canada").
country_name("canada").
finance(3200).

service_(alice_employer_s3306_c_A_neg).
patient_(alice_employer_s3306_c_A_neg,alice_s3306_c_A_neg).
agent_(alice_employer_s3306_c_A_neg,bob_s3306_c_A_neg).
start_(alice_employer_s3306_c_A_neg,d2017_02_01).
end_(alice_employer_s3306_c_A_neg,d2017_09_02).
location_(alice_employer_s3306_c_A_neg,"toronto, ontario, canada").
country_("toronto, ontario, canada","canada").
payment_(alice_pays_s3306_c_A_neg).
agent_(alice_pays_s3306_c_A_neg,alice_s3306_c_A_neg).
patient_(alice_pays_s3306_c_A_neg,bob_s3306_c_A_neg).
start_(alice_pays_s3306_c_A_neg,d2017_09_02).
purpose_(alice_pays_s3306_c_A_neg,alice_employer_s3306_c_A_neg).
amount_(alice_pays_s3306_c_A_neg,3200).

% Test
:- \+ s3306_c_A(alice_employer_s3306_c_A_neg,alice_s3306_c_A_neg,bob_s3306_c_A_neg).
:- halt.
% Text
% Alice has paid $3200 to Bob for work done from Feb 1st, 2017 to Sep 2nd, 2017, in Baltimore, Maryland, USA.

% Question
% Section 3306(c)(A) applies to Alice employing Bob for the year 2017. Entailment

% Facts
person(alice_s3306_c_A_pos).
person(bob_s3306_c_A_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_02_01).
date_split(d2017_02_01, 2017, 2, 1).
date(d2017_09_02).
date_split(d2017_09_02, 2017, 9, 2).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

location_name("baltimore, maryland, usa").
country_name("usa").
finance(3200).

service_(alice_employer_s3306_c_A_pos).
patient_(alice_employer_s3306_c_A_pos,alice_s3306_c_A_pos).
agent_(alice_employer_s3306_c_A_pos,bob_s3306_c_A_pos).
start_(alice_employer_s3306_c_A_pos,d2017_02_01).
end_(alice_employer_s3306_c_A_pos,d2017_09_02).
location_(alice_employer_s3306_c_A_pos,"baltimore, maryland, usa").
country_("baltimore, maryland, usa","usa").
payment_(alice_pays_s3306_c_A_pos).
agent_(alice_pays_s3306_c_A_pos,alice_s3306_c_A_pos).
patient_(alice_pays_s3306_c_A_pos,bob_s3306_c_A_pos).
start_(alice_pays_s3306_c_A_pos,d2017_09_02).
purpose_(alice_pays_s3306_c_A_pos,alice_employer_s3306_c_A_pos).
amount_(alice_pays_s3306_c_A_pos,3200).

% Test
:- s3306_c_A(alice_employer_s3306_c_A_pos,alice_s3306_c_A_pos,bob_s3306_c_A_pos).
:- halt.
% Text
% In 2017, Alice was paid $33200. She is allowed a deduction under section 63(c) of $2000 and deductions of $4000 under section 151 for the year 2017.

% Question
% Under section 63(a), Alice's taxable income in 2017 is equal to $31200. Contradiction

% Facts
person(alice_s63_a_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(31200).
finance(33200).
finance(2000).
finance(4000).
finance(6000).

payment_(alice_is_paid_s63_a_neg).
patient_(alice_is_paid_s63_a_neg,alice_s63_a_neg).
start_(alice_is_paid_s63_a_neg,d2017_12_31).
amount_(alice_is_paid_s63_a_neg,33200).
s63_c(alice_s63_a_neg,2017,2000).
s151(alice_s63_a_neg,4000,alice_s63_a_neg,0,2017).

% Test
:- \+ s63_a(alice_s63_a_neg,2017,31200,33200,6000).
:- halt.
% Text
% In 2017, Alice was paid $33200. She is allowed deductions under section 151 of $2000 for the year 2017. She is allowed an itemized deduction of $4252 in 2017.

% Question
% Under section 63(a), Alice's taxable income in 2017 is equal to $26948. Entailment

% Facts
person(alice_s63_a_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).
finance(26948).
finance(2000).
finance(4252).
finance(6252).

payment_(alice_is_paid_s63_a_pos).
patient_(alice_is_paid_s63_a_pos,alice_s63_a_pos).
start_(alice_is_paid_s63_a_pos,d2017_12_31).
amount_(alice_is_paid_s63_a_pos,33200).
s151(alice_s63_a_pos,2000,alice_s63_a_pos,0,2017).
deduction_(itemized_deduction_s63_a_pos).
agent_(itemized_deduction_s63_a_pos,alice_s63_a_pos).
start_(itemized_deduction_s63_a_pos,d2017_12_31).
amount_(itemized_deduction_s63_a_pos,4252).

% Test
:- s63_a(alice_s63_a_pos,2017,26948,33200,6252).
:- halt.
% Text
% In 2017, Alice was paid $33200. For the year 2017, Alice is allowed a basic standard deduction under section 63(c)(2) of $2000 and an additional standard deduction of $3000 under section 63(c)(3) for the year 2017.

% Question
% Under section 63(c)(1), Alice's standard deduction in 2017 is equal to $4000. Contradiction

% Facts
person(alice_s63_c_1_neg).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).
finance(4000).
finance(2000).
finance(3000).

payment_(alice_is_paid_s63_c_1_neg).
patient_(alice_is_paid_s63_c_1_neg,alice_s63_c_1_neg).
start_(alice_is_paid_s63_c_1_neg,d2017_12_31).
amount_(alice_is_paid_s63_c_1_neg,33200).
s63_c_2(alice_s63_c_1_neg,2017,2000).
s63_c_3(alice_s63_c_1_neg,3000,2017).


% Test
:- \+ s63_c_1(alice_s63_c_1_neg,2017,4000).
:- halt.
% Text
% In 2017, Alice was paid $33200. For the year 2017, Alice is allowed a basic standard deduction under section 63(c)(2) of $2000 and an additional standard deduction of $3000 under section 63(c)(3) for the year 2017.

% Question
% Under section 63(c)(1), Alice's standard deduction in 2017 is equal to $5000. Entailment

% Facts
person(alice_s63_c_1_pos).

year(2017).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).
finance(2000).
finance(3000).
finance(5000).

payment_(alice_is_paid_s63_c_1_pos).
patient_(alice_is_paid_s63_c_1_pos,alice_s63_c_1_pos).
start_(alice_is_paid_s63_c_1_pos,d2017_12_31).
amount_(alice_is_paid_s63_c_1_pos,33200).
s63_c_2(alice_s63_c_1_pos,2017,2000).
s63_c_3(alice_s63_c_1_pos,3000,2017).


% Test
:- s63_c_1(alice_s63_c_1_pos,2017,5000).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017, and they file a joint return for 2017.

% Question
% Under section 63(c)(2)(B), Alice's basic standard deduction in 2017 is equal to $4400. Contradiction

% Facts
person(alice_s63_c_2_B_neg).
person(bob_s63_c_2_B_neg).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03,2017,2,3).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).
finance(4400).

payment_(alice_is_paid_s63_c_2_B_neg).
patient_(alice_is_paid_s63_c_2_B_neg,alice_s63_c_2_B_neg).
start_(alice_is_paid_s63_c_2_B_neg,d2017_12_31).
amount_(alice_is_paid_s63_c_2_B_neg,33200).
marriage_(alice_and_bob_s63_c_2_B_neg).
agent_(alice_and_bob_s63_c_2_B_neg,alice_s63_c_2_B_neg).
agent_(alice_and_bob_s63_c_2_B_neg,bob_s63_c_2_B_neg).
start_(alice_and_bob_s63_c_2_B_neg,d2017_02_03).
joint_return_(alice_and_bob_file_a_joint_return_s63_c_2_B_neg).
agent_(alice_and_bob_file_a_joint_return_s63_c_2_B_neg,alice_s63_c_2_B_neg).
agent_(alice_and_bob_file_a_joint_return_s63_c_2_B_neg,bob_s63_c_2_B_neg).
start_(alice_and_bob_file_a_joint_return_s63_c_2_B_neg,d2017_01_01).
end_(alice_and_bob_file_a_joint_return_s63_c_2_B_neg,d2017_12_31).

% Test
:- \+ s63_c_2_B(alice_s63_c_2_B_neg,2017,4400).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice is a head of household for 2017.

% Question
% Under section 63(c)(2)(B), Alice's basic standard deduction in 2017 is equal to $4400. Entailment

% Facts
person(alice_s63_c_2_B_pos).
person(bob_s63_c_2_B_pos).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03,2017,2,3).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).
finance(4400).

payment_(alice_is_paid_s63_c_2_B_pos).
patient_(alice_is_paid_s63_c_2_B_pos,alice_s63_c_2_B_pos).
start_(alice_is_paid_s63_c_2_B_pos,d2017_12_31).
amount_(alice_is_paid_s63_c_2_B_pos,33200).
s2_b(alice_s63_c_2_B_pos,alice_s63_c_2_B_pos,2017).

% Test
:- s63_c_2_B(alice_s63_c_2_B_pos,2017,4400).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017, and they file a joint return for 2017.

% Question
% Under section 63(c)(2)(C), Alice's basic standard deduction in 2017 is equal to $4400. Contradiction

% Facts
person(alice_s63_c_2_C_neg).
person(bob_s63_c_2_C_neg).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03,2017,2,3).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).
finance(4400).

payment_(alice_is_paid_s63_c_2_C_neg).
patient_(alice_is_paid_s63_c_2_C_neg,alice_s63_c_2_C_neg).
start_(alice_is_paid_s63_c_2_C_neg,d2017_12_31).
amount_(alice_is_paid_s63_c_2_C_neg,33200).
marriage_(alice_and_bob_s63_c_2_C_neg).
agent_(alice_and_bob_s63_c_2_C_neg,alice_s63_c_2_C_neg).
agent_(alice_and_bob_s63_c_2_C_neg,bob_s63_c_2_C_neg).
start_(alice_and_bob_s63_c_2_C_neg,d2017_02_03).
joint_return_(alice_and_bob_file_a_joint_return_s63_c_2_C_neg).
agent_(alice_and_bob_file_a_joint_return_s63_c_2_C_neg,alice_s63_c_2_C_neg).
agent_(alice_and_bob_file_a_joint_return_s63_c_2_C_neg,bob_s63_c_2_C_neg).
start_(alice_and_bob_file_a_joint_return_s63_c_2_C_neg,d2017_01_01).
end_(alice_and_bob_file_a_joint_return_s63_c_2_C_neg,d2017_12_31).

% Test
:- \+ s63_c_2_C(2017,4400).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017. Alice and Bob file separate returns.

% Question
% Under section 63(c)(2)(C), Alice's basic standard deduction in 2017 is equal to $3000. Entailment

% Facts
person(alice_s63_c_2_C_pos).
person(bob_s63_c_2_C_pos).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03,2017,2,3).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).
finance(3000).

payment_(alice_is_paid_s63_c_2_C_pos).
patient_(alice_is_paid_s63_c_2_C_pos,alice_s63_c_2_C_pos).
start_(alice_is_paid_s63_c_2_C_pos,d2017_12_31).
amount_(alice_is_paid_s63_c_2_C_pos,33200).
marriage_(alice_and_bob_s63_c_2_C_pos).
agent_(alice_and_bob_s63_c_2_C_pos,alice_s63_c_2_C_pos).
agent_(alice_and_bob_s63_c_2_C_pos,bob_s63_c_2_C_pos).
start_(alice_and_bob_s63_c_2_C_pos,d2017_02_03).

% Test
:- s63_c_2_C(2017,3000).
:- halt.
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
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017. Alice is entitled to an additional standard deduction of $600 each for herself and for Bob, under section 63(f)(1)(A) and 63(f)(1)(B), respectively.

% Question
% Under section 63(c)(3), Alice's additional standard deduction in 2017 is equal to $1200. Entailment

% Facts
person(alice_s63_c_3_pos).
person(bob_s63_c_3_pos).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03,2017,2,3).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).
finance(1200).

payment_(alice_is_paid_s63_c_3_pos).
patient_(alice_is_paid_s63_c_3_pos,alice_s63_c_3_pos).
start_(alice_is_paid_s63_c_3_pos,d2017_12_31).
amount_(alice_is_paid_s63_c_3_pos,33200).
marriage_(alice_and_bob_s63_c_3_pos).
agent_(alice_and_bob_s63_c_3_pos,alice_s63_c_3_pos).
agent_(alice_and_bob_s63_c_3_pos,bob_s63_c_3_pos).
start_(alice_and_bob_s63_c_3_pos,d2017_02_03).
s63_f_1_A(alice_s63_c_3_pos,2017).
s63_f_1_B(alice_s63_c_3_pos,bob_s63_c_3_pos,2017).

% Test
:- s63_c_3(alice_s63_c_3_pos,1200,2017).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017. Bob earned $10 in 2017. Alice and Bob file separate returns. Alice is not entitled to a deduction for Bob under section 151.

% Question
% Section 63(c)(5) applies to Bob's basic standard deduction in 2017. Contradiction

% Facts
person(alice_s63_c_5_neg).
person(bob_s63_c_5_neg).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03,2017,2,3).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).
finance(10).
finance(500).


payment_(alice_is_paid_s63_c_5_neg).
patient_(alice_is_paid_s63_c_5_neg,alice_s63_c_5_neg).
start_(alice_is_paid_s63_c_5_neg,d2017_12_31).
amount_(alice_is_paid_s63_c_5_neg,33200).
payment_(bob_is_paid_s63_c_5_neg).
patient_(bob_is_paid_s63_c_5_neg,bob_s63_c_5_neg).
start_(bob_is_paid_s63_c_5_neg,d2017_12_31).
amount_(bob_is_paid_s63_c_5_neg,10).
marriage_(alice_and_bob_s63_c_5_neg).
agent_(alice_and_bob_s63_c_5_neg,alice_s63_c_5_neg).
agent_(alice_and_bob_s63_c_5_neg,bob_s63_c_5_neg).
start_(alice_and_bob_s63_c_5_neg,d2017_02_03).

% Test
:- \+ s63_c_5(bob_s63_c_5_neg,0,10,2017,500).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017. Alice is entitled to a deduction for Bob under section 151(b). Bob had no gross income in 2017.

% Question
% Under section 63(c)(5), Bob's basic standard deduction in 2017 is equal to at most $500. Entailment

% Facts
person(alice_s63_c_5_pos).
person(bob_s63_c_5_pos).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03,2017,2,3).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).
finance(500).

payment_(alice_is_paid_s63_c_5_pos).
patient_(alice_is_paid_s63_c_5_pos,alice_s63_c_5_pos).
start_(alice_is_paid_s63_c_5_pos,d2017_12_31).
amount_(alice_is_paid_s63_c_5_pos,33200).
marriage_(alice_and_bob_s63_c_5_pos).
agent_(alice_and_bob_s63_c_5_pos,alice_s63_c_5_pos).
agent_(alice_and_bob_s63_c_5_pos,bob_s63_c_5_pos).
start_(alice_and_bob_s63_c_5_pos,d2017_02_03).
s151_b_applies(alice_s63_c_5_pos,bob_s63_c_5_pos,2017).

% Test
:- s63_c_5(bob_s63_c_5_pos,0,0,2017,500).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017. Bob and Alice file a joint return for 2017.

% Question
% Section 63(c)(6)(A) applies to Alice for 2017. Contradiction

% Facts
person(alice_s63_c_6_A_neg).
person(bob_s63_c_6_A_neg).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03,2017,2,3).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).

payment_(alice_is_paid_s63_c_6_A_neg).
patient_(alice_is_paid_s63_c_6_A_neg,alice_s63_c_6_A_neg).
start_(alice_is_paid_s63_c_6_A_neg,d2017_12_31).
amount_(alice_is_paid_s63_c_6_A_neg,33200).
marriage_(alice_and_bob_s63_c_6_A_neg).
agent_(alice_and_bob_s63_c_6_A_neg,alice_s63_c_6_A_neg).
agent_(alice_and_bob_s63_c_6_A_neg,bob_s63_c_6_A_neg).
start_(alice_and_bob_s63_c_6_A_neg,d2017_02_03).
joint_return_(bob_and_alice_joint_return_s63_c_6_A_neg).
agent_(bob_and_alice_joint_return_s63_c_6_A_neg,bob_s63_c_6_A_neg).
agent_(bob_and_alice_joint_return_s63_c_6_A_neg,alice_s63_c_6_A_neg).
start_(bob_and_alice_joint_return_s63_c_6_A_neg,d2017_01_01).
end_(bob_and_alice_joint_return_s63_c_6_A_neg,d2017_12_31).
deduction_(random_deduction).

% Test
:- \+ s63_c_6_A(alice_s63_c_6_A_neg,bob_s63_c_6_A_neg,random_deduction,2017).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017. Bob is allowed an itemized deduction of $4324. Alice and Bob file separate returns.

% Question
% Section 63(c)(6)(A) applies to Alice for 2017. Entailment

% Facts
person(alice_s63_c_6_A_pos).
person(bob_s63_c_6_A_pos).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03,2017,2,3).
date(d2017_01_01).
date_split(d2017_01_01,2017,1,1).
date(d2017_12_31).
date_split(d2017_12_31,2017,12,31).

finance(33200).

payment_(alice_is_paid_s63_c_6_A_pos).
patient_(alice_is_paid_s63_c_6_A_pos,alice_s63_c_6_A_pos).
start_(alice_is_paid_s63_c_6_A_pos,d2017_12_31).
amount_(alice_is_paid_s63_c_6_A_pos,33200).
marriage_(alice_and_bob_s63_c_6_A_pos).
agent_(alice_and_bob_s63_c_6_A_pos,alice_s63_c_6_A_pos).
agent_(alice_and_bob_s63_c_6_A_pos,bob_s63_c_6_A_pos).
start_(alice_and_bob_s63_c_6_A_pos,d2017_02_03).
deduction_(bob_itemized_deduction_s63_c_6_A_pos).
agent_(bob_itemized_deduction_s63_c_6_A_pos,bob_s63_c_6_A_pos).
start_(bob_itemized_deduction_s63_c_6_A_pos,d2017_12_31).

% Test
:- s63_c_6_A(alice_s63_c_6_A_pos,bob_s63_c_6_A_pos,bob_itemized_deduction_s63_c_6_A_pos,2017).
:- halt.
% Text
% In 2019, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2019.  Alice and Bob file separate returns in 2019.

% Question
% Under section 63(c)(7)(ii), Alice's basic standard deduction in 2019 is equal to $3000. Contradiction

% Facts
person(alice_s63_c_7_ii_neg).
person(bob_s63_c_7_ii_neg).
finance(33200).
finance(3000).

year(2019).
date(d2019_02_03).
date_split(d2019_02_03, 2019, 2, 3).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

payment_(alice_is_paid_s63_c_7_ii_neg).
patient_(alice_is_paid_s63_c_7_ii_neg,alice_s63_c_7_ii_neg).
start_(alice_is_paid_s63_c_7_ii_neg,d2019_12_31).
amount_(alice_is_paid_s63_c_7_ii_neg,33200).
marriage_(alice_and_bob_s63_c_7_ii_neg).
agent_(alice_and_bob_s63_c_7_ii_neg,alice_s63_c_7_ii_neg).
agent_(alice_and_bob_s63_c_7_ii_neg,bob_s63_c_7_ii_neg).
start_(alice_and_bob_s63_c_7_ii_neg,d2019_02_03).

% Test
:- \+ s63_c_7_ii(2019,3000).
:- halt.
% Text
% In 2019, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2019. Alice and Bob file separate returns in 2019.

% Question
% Under section 63(c)(7)(ii), Alice's basic standard deduction in 2019 is equal to $12000. Entailment

% Facts
person(alice_s63_c_7_ii_pos).
person(bob_s63_c_7_ii_pos).
finance(33200).
finance(12000).

year(2019).
date(d2019_02_03).
date_split(d2019_02_03, 2019, 2, 3).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

payment_(alice_is_paid_s63_c_7_ii_pos).
patient_(alice_is_paid_s63_c_7_ii_pos,alice_s63_c_7_ii_pos).
start_(alice_is_paid_s63_c_7_ii_pos,d2019_12_31).
amount_(alice_is_paid_s63_c_7_ii_pos,33200).
marriage_(alice_and_bob_s63_c_7_ii_pos).
agent_(alice_and_bob_s63_c_7_ii_pos,alice_s63_c_7_ii_pos).
agent_(alice_and_bob_s63_c_7_ii_pos,bob_s63_c_7_ii_pos).
start_(alice_and_bob_s63_c_7_ii_pos,d2019_02_03).

% Test
:- s63_c_7_ii(2019,12000).
:- halt.
% Text
% In 2017, Alice was paid $33200 in remuneration. She is allowed deductions under section 63(c)(3) of $1200 for the year 2017.

% Question
% Alice's deduction for 2017 falls under section 63(d)(2). Contradiction

% Facts
person(alice_s63_d_2_neg).
finance(33200).
finance(1200).

year(2017).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(2019).
date(d2019_02_03).
date_split(d2019_02_03, 2019, 2, 3).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

payment_(alice_is_paid_s63_d_2_neg).
patient_(alice_is_paid_s63_d_2_neg,alice_s63_d_2_neg).
start_(alice_is_paid_s63_d_2_neg,d2017_12_31).
amount_(alice_is_paid_s63_d_2_neg,33200).
s63_c_3(alice_s63_d_2_neg,1200,2017).

% Test
:- \+ s63_d_2(alice_s63_d_2_neg,1200,2017).
:- halt.
% Text
% In 2017, Alice was paid $33200 in remuneration. She is allowed a deduction for herself under section 151 of $2000 for the year 2017.

% Question
% Alice's deduction for 2017 falls under section 63(d)(2). Entailment

% Facts
person(alice_s63_d_2_pos).
finance(33200).
finance(2000).

year(2017).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

payment_(alice_is_paid_s63_d_2_pos).
patient_(alice_is_paid_s63_d_2_pos,alice_s63_d_2_pos).
start_(alice_is_paid_s63_d_2_pos,d2017_12_31).
amount_(alice_is_paid_s63_d_2_pos,33200).
s151(alice_s63_d_2_pos,2000,alice_s63_d_2_pos,0,2017).

% Test
:- s63_d_2(alice_s63_d_2_pos,2000,2017).
:- halt.
% Text
% In 2017, Alice was paid $33200. She is allowed a deduction of $2000 for herself for the year 2017 under section 151(b).

% Question
% Alice's deduction for 2017 falls under section 63(d). Contradiction

% Facts
person(alice_s63_d_neg).
finance(33200).
finance(2000).

year(2017).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

payment_(alice_is_paid_s63_d_neg).
patient_(alice_is_paid_s63_d_neg,alice_s63_d_neg).
start_(alice_is_paid_s63_d_neg,d2017_12_31).
amount_(alice_is_paid_s63_d_neg,33200).
s151_b(alice_s63_d_neg,2000,2017).

% Test
:- \+ s63_d(alice_s63_d_neg,2000,2000,2017).
:- halt.
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
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017. Alice was born March 2nd, 1950 and Bob was born March 3rd, 1955. In addition, Alice is allowed an exemption for Bob under section 151(b) for the year 2017.

% Question
% Section 63(f)(1)(B) applies to Alice with Bob as the spouse in 2017. Contradiction

% Facts
person(alice_s63_f_1_B_neg).
person(bob_s63_f_1_B_neg).
finance(33200).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03, 2017, 2, 3).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(1950).
date(d1950_03_02).
date_split(d1950_03_02, 1950, 3, 2).
date(d1950_01_01).
date_split(d1950_01_01, 1950, 1, 1).
date(d1950_12_31).
date_split(d1950_12_31, 1950, 12, 31).

year(1955).
date(d1955_03_03).
date_split(d1955_03_03, 1955, 3, 3).
date(d1955_01_01).
date_split(d1955_01_01, 1955, 1, 1).
date(d1955_12_31).
date_split(d1955_12_31, 1955, 12, 31).

payment_(alice_is_paid_s63_f_1_B_neg).
patient_(alice_is_paid_s63_f_1_B_neg,alice_s63_f_1_B_neg).
start_(alice_is_paid_s63_f_1_B_neg,d2017_12_31).
amount_(alice_is_paid_s63_f_1_B_neg,33200).
marriage_(alice_and_bob_s63_f_1_B_neg).
agent_(alice_and_bob_s63_f_1_B_neg,alice_s63_f_1_B_neg).
agent_(alice_and_bob_s63_f_1_B_neg,bob_s63_f_1_B_neg).
start_(alice_and_bob_s63_f_1_B_neg,d2017_02_03).
birth_(alice_is_born_s63_f_1_B_neg).
agent_(alice_is_born_s63_f_1_B_neg,alice_s63_f_1_B_neg).
start_(alice_is_born_s63_f_1_B_neg,d1950_03_02).
end_(alice_is_born_s63_f_1_B_neg,d1950_03_02).
birth_(bob_is_born_s63_f_1_B_neg).
agent_(bob_is_born_s63_f_1_B_neg,bob_s63_f_1_B_neg).
start_(bob_is_born_s63_f_1_B_neg,d1955_03_03).
end_(bob_is_born_s63_f_1_B_neg,d1955_03_03).
s151_b_applies(alice_s63_f_1_B_neg,bob_s63_f_1_B_neg,2017).

% Test
:- \+ s63_f_1_B(alice_s63_f_1_B_neg,bob_s63_f_1_B_neg,2017).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017. Alice was born March 2nd, 1950 and Bob was born March 3rd, 1955. In addition, Bob is allowed an exemption for Alice under section 151(b) for the year 2017.

% Question
% Section 63(f)(1)(B) applies to Bob with Alice as the spouse in 2017. Entailment

% Facts
person(alice_s63_f_1_B_pos).
person(bob_s63_f_1_B_pos).
finance(33200).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03, 2017, 2, 3).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

year(1950).
date(d1950_03_02).
date_split(d1950_03_02, 1950, 3, 2).
date(d1950_01_01).
date_split(d1950_01_01, 1950, 1, 1).
date(d1950_12_31).
date_split(d1950_12_31, 1950, 12, 31).

year(1955).
date(d1955_03_03).
date_split(d1955_03_03, 1955, 3, 3).
date(d1955_01_01).
date_split(d1955_01_01, 1955, 1, 1).
date(d1955_12_31).
date_split(d1955_12_31, 1955, 12, 31).

payment_(alice_is_paid_s63_f_1_B_pos).
patient_(alice_is_paid_s63_f_1_B_pos,alice_s63_f_1_B_pos).
start_(alice_is_paid_s63_f_1_B_pos,d2017_12_31).
amount_(alice_is_paid_s63_f_1_B_pos,33200).
marriage_(alice_and_bob_s63_f_1_B_pos).
agent_(alice_and_bob_s63_f_1_B_pos,alice_s63_f_1_B_pos).
agent_(alice_and_bob_s63_f_1_B_pos,bob_s63_f_1_B_pos).
start_(alice_and_bob_s63_f_1_B_pos,d2017_02_03).
birth_(alice_is_born_s63_f_1_B_pos).
agent_(alice_is_born_s63_f_1_B_pos,alice_s63_f_1_B_pos).
start_(alice_is_born_s63_f_1_B_pos,d1950_03_02).
end_(alice_is_born_s63_f_1_B_pos,d1950_03_02).
birth_(bob_is_born_s63_f_1_B_pos).
agent_(bob_is_born_s63_f_1_B_pos,bob_s63_f_1_B_pos).
start_(bob_is_born_s63_f_1_B_pos,d1955_03_03).
end_(bob_is_born_s63_f_1_B_pos,d1955_03_03).
s151_b_applies(bob_s63_f_1_B_pos,alice_s63_f_1_B_pos,2017).

% Test
:- s63_f_1_B(bob_s63_f_1_B_pos,alice_s63_f_1_B_pos,2017).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017. Alice and Bob file separate returns in 2017. Alice has been blind since April 19, 2015.

% Question
% Section 63(f)(2)(A) applies to Bob in 2017. Contradiction

% Facts
person(alice_s63_f_2_A_neg).
person(bob_s63_f_2_A_neg).
finance(33200).

year(2015).
date(d2015_04_19).
date_split(d2015_04_19, 2015, 4, 19).
date(d2015_01_01).
date_split(d2015_01_01, 2015, 1, 1).
date(d2015_12_31).
date_split(d2015_12_31, 2015, 12, 31).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03, 2017, 2, 3).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).


payment_(alice_is_paid_s63_f_2_A_neg).
patient_(alice_is_paid_s63_f_2_A_neg,alice_s63_f_2_A_neg).
start_(alice_is_paid_s63_f_2_A_neg,d2017_12_31).
amount_(alice_is_paid_s63_f_2_A_neg,33200).
marriage_(alice_and_bob_s63_f_2_A_neg).
agent_(alice_and_bob_s63_f_2_A_neg,alice_s63_f_2_A_neg).
agent_(alice_and_bob_s63_f_2_A_neg,bob_s63_f_2_A_neg).
start_(alice_and_bob_s63_f_2_A_neg,d2017_02_03).
blindness_(alice_is_blind_s63_f_2_A_neg).
agent_(alice_is_blind_s63_f_2_A_neg,alice_s63_f_2_A_neg).
start_(alice_is_blind_s63_f_2_A_neg,d2015_04_19).

% Test
:- \+ s63_f_2_A(bob_s63_f_2_A_neg,2017).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice and Bob have been married since Feb 3rd, 2017. Alice has been blind since March 20, 2016.

% Question
% Section 63(f)(2)(A) applies to Alice in 2017. Entailment

% Facts
person(alice_s63_f_2_A_pos).
person(bob_s63_f_2_A_pos).
finance(33200).

year(2016).
date(d2016_03_20).
date_split(d2016_03_20, 2016, 3, 20).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03, 2017, 2, 3).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

payment_(alice_is_paid_s63_f_2_A_pos).
patient_(alice_is_paid_s63_f_2_A_pos,alice_s63_f_2_A_pos).
start_(alice_is_paid_s63_f_2_A_pos,d2017_12_31).
amount_(alice_is_paid_s63_f_2_A_pos,33200).
marriage_(alice_and_bob_s63_f_2_A_pos).
agent_(alice_and_bob_s63_f_2_A_pos,alice_s63_f_2_A_pos).
agent_(alice_and_bob_s63_f_2_A_pos,bob_s63_f_2_A_pos).
start_(alice_and_bob_s63_f_2_A_pos,d2017_02_03).
blindness_(alice_is_blind_s63_f_2_A_pos).
agent_(alice_is_blind_s63_f_2_A_pos,alice_s63_f_2_A_pos).
start_(alice_is_blind_s63_f_2_A_pos,d2016_03_20).

% Test
:- s63_f_2_A(alice_s63_f_2_A_pos,2017).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice was born March 2nd, 1950 and Bob was born March 3rd, 1955.

% Question
% Under section 63(f)(3), Alice's additional standard deduction in 2017 is equal to $600. Contradiction

% Facts
person(alice_s63_f_3_neg).
person(bob_s63_f_3_neg).
finance(33200).
finance(600).

year(1950).
date(d1950_03_02).
date_split(d1950_03_02, 1950, 3, 2).
date(d1950_01_01).
date_split(d1950_01_01, 1950, 1, 1).
date(d1950_12_31).
date_split(d1950_12_31, 1950, 12, 31).

year(1955).
date(d1955_03_03).
date_split(d1955_03_03, 1955, 3, 3).
date(d1955_01_01).
date_split(d1955_01_01, 1955, 1, 1).
date(d1955_12_31).
date_split(d1955_12_31, 1955, 12, 31).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03, 2017, 2, 3).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

payment_(alice_is_paid_s63_f_3_neg).
patient_(alice_is_paid_s63_f_3_neg,alice_s63_f_3_neg).
start_(alice_is_paid_s63_f_3_neg,d2017_12_31).
amount_(alice_is_paid_s63_f_3_neg,33200).
birth_(alice_is_born_s63_f_3_neg).
agent_(alice_is_born_s63_f_3_neg,alice_s63_f_3_neg).
start_(alice_is_born_s63_f_3_neg,d1950_03_02).
end_(alice_is_born_s63_f_3_neg,d1950_03_02).
birth_(bob_is_born_s63_f_3_neg).
agent_(bob_is_born_s63_f_3_neg,bob_s63_f_3_neg).
start_(bob_is_born_s63_f_3_neg,d1955_03_03).
end_(bob_is_born_s63_f_3_neg,d1955_03_03).

% Test
:- \+ s63_f_3(alice_s63_f_3_neg,2017,600).
:- halt.
% Text
% In 2017, Alice was paid $33200. Alice was born March 2nd, 1950 and Bob was born March 3rd, 1955.

% Question
% Under section 63(f)(3), Alice's additional standard deduction in 2017 is equal to $750. Entailment

% Facts
person(alice_s63_f_3_pos).
person(bob_s63_f_3_pos).
finance(33200).
finance(750).

year(1950).
date(d1950_03_02).
date_split(d1950_03_02, 1950, 3, 2).
date(d1950_01_01).
date_split(d1950_01_01, 1950, 1, 1).
date(d1950_12_31).
date_split(d1950_12_31, 1950, 12, 31).

year(1955).
date(d1955_03_03).
date_split(d1955_03_03, 1955, 3, 3).
date(d1955_01_01).
date_split(d1955_01_01, 1955, 1, 1).
date(d1955_12_31).
date_split(d1955_12_31, 1955, 12, 31).

year(2017).
date(d2017_02_03).
date_split(d2017_02_03, 2017, 2, 3).
date(d2017_01_01).
date_split(d2017_01_01, 2017, 1, 1).
date(d2017_12_31).
date_split(d2017_12_31, 2017, 12, 31).

payment_(alice_is_paid_s63_f_3_pos).
patient_(alice_is_paid_s63_f_3_pos,alice_s63_f_3_pos).
start_(alice_is_paid_s63_f_3_pos,d2017_12_31).
amount_(alice_is_paid_s63_f_3_pos,33200).
birth_(alice_is_born_s63_f_3_pos).
agent_(alice_is_born_s63_f_3_pos,alice_s63_f_3_pos).
start_(alice_is_born_s63_f_3_pos,d1950_03_02).
end_(alice_is_born_s63_f_3_pos,d1950_03_02).
birth_(bob_is_born_s63_f_3_pos).
agent_(bob_is_born_s63_f_3_pos,bob_s63_f_3_pos).
start_(bob_is_born_s63_f_3_pos,d1955_03_03).
end_(bob_is_born_s63_f_3_pos,d1955_03_03).

% Test
:- s63_f_3(alice_s63_f_3_pos,2017,750).
:- halt.
% Text
% In 2016, Alice's income was $267192. Alice is a head of household for the year 2016. Alice is allowed itemized deductions of $60000 under section 63.

% Question
% Section 68(a)(1) prescribes a reduction of Alice's itemized deductions for the year 2016 by $306. Contradiction

% Facts
person(alice_s68_a_1_neg).
finance(267192).
finance(275000).
finance(306).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

income_(alice_is_paid_s68_a_1_neg).
agent_(alice_is_paid_s68_a_1_neg,alice_s68_a_1_neg).
start_(alice_is_paid_s68_a_1_neg,d2016_12_31).
amount_(alice_is_paid_s68_a_1_neg,267192).
s2_b(alice_s68_a_1_neg,alice_s68_a_1_neg,2016).
gross_income(alice_s68_a_1_neg,2016,267192).
s68_b(alice_s68_a_1_neg,275000,2016).

% Test
:- \+ s68_a_1(267192,275000,306).
:- halt.
% Text
% In 2016, Alice's income was $310192. Alice is a surviving spouse for the year 2016. Alice is allowed itemized deductions of $60000 under section 63.

% Question
% Section 68(a)(1) prescribes a reduction of Alice's itemized deductions for the year 2016 by $306. Entailment

% Facts
person(alice_s68_a_1_pos).
person(spouse_s68_a_1_pos).
finance(310192).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

income_(alice_is_paid_s68_a_1_pos).
agent_(alice_is_paid_s68_a_1_pos,alice_s68_a_1_pos).
start_(alice_is_paid_s68_a_1_pos,d2016_12_31).
amount_(alice_is_paid_s68_a_1_pos,310192).
s2_a(alice_s68_a_1_pos,spouse_s68_a_1_pos,2016).
s68_b(alice_s68_a_1_pos,300000,2016).
gross_income(alice_s68_a_1_pos,2016,310192).

% Test
:- s68_a_1(310192,300000,306).
:- halt.
% Text
% In 2016, Alice's income was $567192. Alice is married for the year 2016 under section 7703. Alice does not file a joint return.

% Question
% Section 68(b)(1)(A) applies to Alice for 2016. Contradiction

% Facts
person(alice_s68_b_1_A_neg).
person(bob_s68_b_1_A_neg).
marriage_(alice_and_bob_s68_b_1_A_neg).
finance(567192).
finance(300000).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

income_(alice_is_paid_s68_b_1_A_neg).
agent_(alice_is_paid_s68_b_1_A_neg,alice_s68_b_1_A_neg).
start_(alice_is_paid_s68_b_1_A_neg,d2016_12_31).
amount_(alice_is_paid_s68_b_1_A_neg,567192).
s7703(alice_s68_b_1_A_neg,bob_s68_b_1_A_neg,alice_and_bob_s68_b_1_A_neg,2016).
joint_return_(random_joint_return).

% Test
:- \+ s68_b_1_A(alice_s68_b_1_A_neg,random_joint_return,bob_s68_b_1_A_neg,300000,2016).
:- halt.
% Text
% In 2016, Alice's income was $567192. Alice is a surviving spouse for the year 2016.

% Question
% Under section 68(b)(1)(A), Alice's applicable amount for 2016 is equal to $300000. Entailment

% Facts
person(alice_s68_b_1_A_pos).
person(spouse_s68_b_1_A_pos).
finance(567192).
finance(300000).


year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

income_(alice_is_paid_s68_b_1_A_pos).
agent_(alice_is_paid_s68_b_1_A_pos,alice_s68_b_1_A_pos).
start_(alice_is_paid_s68_b_1_A_pos,d2016_12_31).
amount_(alice_is_paid_s68_b_1_A_pos,567192).
s2_a(alice_s68_b_1_A_pos,spouse_s68_b_1_A_pos,2016).
joint_return_(random_joint_return).

% Test
:- s68_b_1_A(alice_s68_b_1_A_pos,random_joint_return,alice_s68_b_1_A_pos,300000,2016).
:- halt.
% Text
% In 2016, Alice's income was $567192. Alice is not married.

% Question
% Section 68(b)(1)(D) applies to Alice in 2016. Contradiction

% Facts
person(alice_s68_b_1_D_neg).
person(bob_s68_b_1_D_neg).
finance(567192).
finance(150000).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

income_(alice_is_paid_s68_b_1_D_neg).
agent_(alice_is_paid_s68_b_1_D_neg,alice_s68_b_1_D_neg).
start_(alice_is_paid_s68_b_1_D_neg,d2016_12_31).
amount_(alice_is_paid_s68_b_1_D_neg,567192).
s2_a(alice_s68_b_1_D_neg,bob_s68_b_1_D_neg,2016).

% Test
:- \+ s68_b_1_D(alice_s68_b_1_D_neg,150000,2016).
:- halt.
% Text
% In 2016, Alice's income was $567192. Alice is married for the year 2016 under section 7703. Alice does not file a joint return.

% Question
% Under section 68(b)(1)(D), Alice's applicable amount for 2016 is equal to $150000. Entailment

% Facts
person(alice_s68_b_1_D_pos).
person(bob_s68_b_1_D_pos).
finance(567192).
finance(150000).

year(2016).
date(d2016_01_01).
date_split(d2016_01_01, 2016, 1, 1).
date(d2016_12_31).
date_split(d2016_12_31, 2016, 12, 31).

income_(alice_is_paid_s68_b_1_D_pos).
agent_(alice_is_paid_s68_b_1_D_pos,alice_s68_b_1_D_pos).
start_(alice_is_paid_s68_b_1_D_pos,d2016_12_31).
amount_(alice_is_paid_s68_b_1_D_pos,567192).
marriage_(alice_and_bob_s68_b_1_D_pos),
agent_(alice_and_bob_s68_b_1_D_pos,alice_s68_b_1_D_pos),
agent_(alice_and_bob_s68_b_1_D_pos,bob_s68_b_1_D_pos),
s7703(alice_s68_b_1_D_pos,bob_s68_b_1_D_pos,alice_and_bob_s68_b_1_D_pos,2016).

% Test
:- s68_b_1_D(alice_s68_b_1_D_pos,150000,2016).
:- halt.
% Text
% In 2014, Alice's income was $310192. Alice is a surviving spouse for the year 2014. Alice is allowed itemized deductions of $600 under section 63.

% Question
% Section 68(f) applies to Alice for the year 2014. Contradiction

% Facts
person(alice_s68_f_neg).
person(bob_s68_f_neg).
finance(310192).

year(2014).
date(d2014_01_01).
date_split(d2014_01_01, 2014, 1, 1).
date(d2014_12_31).
date_split(d2014_12_31, 2014, 12, 31).

income_(alice_is_paid_s68_f_neg).
agent_(alice_is_paid_s68_f_neg,alice_s68_f_neg).
start_(alice_is_paid_s68_f_neg,d2014_12_31).
amount_(alice_is_paid_s68_f_neg,310192).
s2_a(alice_s68_f_neg,bob_s68_f_neg,2014).

% Test
:- \+ s68_f(2014).
:- halt.
% Text
% In 2018, Alice's income was $310192. Alice is a surviving spouse for the year 2018. Alice is allowed itemized deductions of $600 under section 63.

% Question
% Section 68(f) applies to Alice for the year 2018. Entailment

% Facts
person(alice_s68_f_pos).
person(bob_s68_f_pos).
finance(310192).

year(2018).
date(d2018_01_01).
date_split(d2018_01_01, 2018, 1, 1).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

income_(alice_is_paid_s68_f_pos).
agent_(alice_is_paid_s68_f_pos,alice_s68_f_pos).
start_(alice_is_paid_s68_f_pos,d2018_12_31).
amount_(alice_is_paid_s68_f_pos,310192).
s2_a(alice_s68_f_pos,bob_s68_f_pos,2018).

% Test
:- s68_f(2018).
:- halt.
% Text
% Alice and Bob got married on April 5th, 2012. Alice and Bob were legally separated under a decree of divorce on September 16th, 2017.

% Question
% Section 7703(a)(2) applies to Alice for the year 2012. Contradiction

% Facts
person(alice_s7703_a_2_neg).
person(bob_s7703_a_2_neg).

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

marriage_(alice_and_bob_s7703_a_2_neg).
agent_(alice_and_bob_s7703_a_2_neg,alice_s7703_a_2_neg).
agent_(alice_and_bob_s7703_a_2_neg,bob_s7703_a_2_neg).
start_(alice_and_bob_s7703_a_2_neg,d2012_04_05).
legal_separation_(alice_and_bob_divorce_s7703_a_2_neg).
patient_(alice_and_bob_divorce_s7703_a_2_neg,alice_and_bob_s7703_a_2_neg).
agent_(alice_and_bob_divorce_s7703_a_2_neg,"decree of divorce").
start_(alice_and_bob_divorce_s7703_a_2_neg,d2017_09_16).

% Test
:- \+ s7703_a_2(alice_s7703_a_2_neg,bob_s7703_a_2_neg,alice_and_bob_s7703_a_2_neg,alice_and_bob_divorce_s7703_a_2_neg,2012).
:- halt.
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
agent_(alice_and_bob_divorce_s7703_a_2_pos,"decree of divorce").
start_(alice_and_bob_divorce_s7703_a_2_pos,d2017_09_16).

% Test
:- s7703_a_2(alice_s7703_a_2_pos,bob_s7703_a_2_pos,alice_and_bob_s7703_a_2_pos,alice_and_bob_divorce_s7703_a_2_pos,2018).
:- halt.
% Text
% Alice and Bob got married on April 5th, 2012. Alice and Bob have a son, Charlie, who was born on September 16th, 2017. Alice and Charlie live in a home maintained by Alice since September 16th, 2017. Alice is entitled to a deduction for Charlie under section 151(c) for the years 2017 to 2019. Alice and Bob file a joint return for the years 2017 to 2019.

% Question
% Section 7703(b)(1) applies to Alice for the year 2018. Contradiction

% Facts
person(alice_s7703_b_1_neg).
person(bob_s7703_b_1_neg).
person(charlie_s7703_b_1_neg).

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

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

household(alice_s_house_s7703_b_1_neg).
finance(1).

marriage_(alice_and_bob_s7703_b_1_neg).
agent_(alice_and_bob_s7703_b_1_neg,alice_s7703_b_1_neg).
agent_(alice_and_bob_s7703_b_1_neg,bob_s7703_b_1_neg).
start_(alice_and_bob_s7703_b_1_neg,d2012_04_05).
son_(charlie_is_born_s7703_b_1_neg).
agent_(charlie_is_born_s7703_b_1_neg,charlie_s7703_b_1_neg).
patient_(charlie_is_born_s7703_b_1_neg,bob_s7703_b_1_neg).
patient_(charlie_is_born_s7703_b_1_neg,alice_s7703_b_1_neg).
start_(charlie_is_born_s7703_b_1_neg,d2017_09_16).
residence_(charlie_residence_s7703_b_1_neg).
agent_(charlie_residence_s7703_b_1_neg,charlie_s7703_b_1_neg).
patient_(charlie_residence_s7703_b_1_neg,alice_s_house_s7703_b_1_neg).
start_(charlie_residence_s7703_b_1_neg,d2017_09_16).
residence_(alice_residence_s7703_b_1_neg).
agent_(alice_residence_s7703_b_1_neg,alice_s7703_b_1_neg).
patient_(alice_residence_s7703_b_1_neg,alice_s_house_s7703_b_1_neg).
start_(alice_residence_s7703_b_1_neg,d2017_09_16).

% NOTE: should be generated to 2117 + dates should be validated
alice_household_maintenance(2017,'alice_maintains_household_s7703_b_1_neg2017',d2017_09_16,"2017-12-31").
alice_household_maintenance(2018,'alice_maintains_household_s7703_b_1_neg2018',d2018_01_01,"2018-12-31").
alice_household_maintenance(2019,'alice_maintains_household_s7703_b_1_neg2019',d2019_01_01,"2019-12-31").
alice_household_maintenance(2020,'alice_maintains_household_s7703_b_1_neg2020',d2020_01_01,"2020-12-31").
alice_household_maintenance(2021,'alice_maintains_household_s7703_b_1_neg2021',d2021_01_01,"2021-12-31").
alice_household_maintenance(2022,'alice_maintains_household_s7703_b_1_neg2022',d2022_01_01,"2022-12-31").
alice_household_maintenance(2023,'alice_maintains_household_s7703_b_1_neg2023',d2023_01_01,"2023-12-31").
alice_household_maintenance(2024,'alice_maintains_household_s7703_b_1_neg2024',d2024_01_01,"2024-12-31").
alice_household_maintenance(2025,'alice_maintains_household_s7703_b_1_neg2025',d2025_01_01,"2025-12-31").
alice_household_maintenance(2026,'alice_maintains_household_s7703_b_1_neg2026',d2026_01_01,"2026-12-31").
alice_household_maintenance(2027,'alice_maintains_household_s7703_b_1_neg2027',d2027_01_01,"2027-12-31").
alice_household_maintenance(2028,'alice_maintains_household_s7703_b_1_neg2028',d2028_01_01,"2028-12-31").
alice_household_maintenance(2029,'alice_maintains_household_s7703_b_1_neg2029',d2029_01_01,"2029-12-31").
alice_household_maintenance(2030,'alice_maintains_household_s7703_b_1_neg2030',d2030_01_01,"2030-12-31").
alice_household_maintenance(2031,'alice_maintains_household_s7703_b_1_neg2031',d2031_01_01,"2031-12-31").
alice_household_maintenance(2032,'alice_maintains_household_s7703_b_1_neg2032',d2032_01_01,"2032-12-31").
alice_household_maintenance(2033,'alice_maintains_household_s7703_b_1_neg2033',d2033_01_01,"2033-12-31").
alice_household_maintenance(2034,'alice_maintains_household_s7703_b_1_neg2034',d2034_01_01,"2034-12-31").
alice_household_maintenance(2035,'alice_maintains_household_s7703_b_1_neg2035',d2035_01_01,"2035-12-31").
alice_household_maintenance(2036,'alice_maintains_household_s7703_b_1_neg2036',d2036_01_01,"2036-12-31").
alice_household_maintenance(2037,'alice_maintains_household_s7703_b_1_neg2037',d2037_01_01,"2037-12-31").
alice_household_maintenance(2038,'alice_maintains_household_s7703_b_1_neg2038',d2038_01_01,"2038-12-31").
alice_household_maintenance(2039,'alice_maintains_household_s7703_b_1_neg2039',d2039_01_01,"2039-12-31").
alice_household_maintenance(2040,'alice_maintains_household_s7703_b_1_neg2040',d2040_01_01,"2040-12-31").
alice_household_maintenance(2041,'alice_maintains_household_s7703_b_1_neg2041',d2041_01_01,"2041-12-31").
alice_household_maintenance(2042,'alice_maintains_household_s7703_b_1_neg2042',d2042_01_01,"2042-12-31").
alice_household_maintenance(2043,'alice_maintains_household_s7703_b_1_neg2043',d2043_01_01,"2043-12-31").
alice_household_maintenance(2044,'alice_maintains_household_s7703_b_1_neg2044',d2044_01_01,"2044-12-31").
alice_household_maintenance(2045,'alice_maintains_household_s7703_b_1_neg2045',d2045_01_01,"2045-12-31").
alice_household_maintenance(2046,'alice_maintains_household_s7703_b_1_neg2046',d2046_01_01,"2046-12-31").
alice_household_maintenance(2047,'alice_maintains_household_s7703_b_1_neg2047',d2047_01_01,"2047-12-31").
alice_household_maintenance(2048,'alice_maintains_household_s7703_b_1_neg2048',d2048_01_01,"2048-12-31").
alice_household_maintenance(2049,'alice_maintains_household_s7703_b_1_neg2049',d2049_01_01,"2049-12-31").
alice_household_maintenance(2050,'alice_maintains_household_s7703_b_1_neg2050',d2050_01_01,"2050-12-31").

% alice_household_maintenance(Year,Event,Start_day,End_day) :-
%     between(2017,2117,Year), % avoid infinite forward loop
%     atom_concat('alice_maintains_household_',Year,Event),
%     (((Year==2017)->(Start_day=d2017_09_16));first_day_year(Year,Start_day)),
%     last_day_year(Year,End_day).

payment_(Event) :- alice_household_maintenance(_,Event,_,_).
agent_(Event,alice_s7703_b_1_neg) :- alice_household_maintenance(_,Event,_,_).
amount_(Event,1) :- alice_household_maintenance(_,Event,_,_).
purpose_(Event,alice_s_house_s7703_b_1_neg) :- alice_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- alice_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- alice_household_maintenance(_,Event,_,End_day).
s151_c_applies(alice_s7703_b_1_neg,charlie_s7703_b_1_neg,Year) :- between(2017,2019,Year).
joint_return_(alice_and_bob_joint_return_2017).
agent_(alice_and_bob_joint_return_2017,alice_s7703_b_1_neg).
agent_(alice_and_bob_joint_return_2017,bob_s7703_b_1_neg).
start_(alice_and_bob_joint_return_2017,d2017_01_01).
end_(alice_and_bob_joint_return_2017,d2017_12_31).
joint_return_(alice_and_bob_joint_return_2018).
agent_(alice_and_bob_joint_return_2018,alice_s7703_b_1_neg).
agent_(alice_and_bob_joint_return_2018,bob_s7703_b_1_neg).
start_(alice_and_bob_joint_return_2018,d2018_01_01).
end_(alice_and_bob_joint_return_2018,d2018_12_31).
joint_return_(alice_and_bob_joint_return_2019).
agent_(alice_and_bob_joint_return_2019,alice_s7703_b_1_neg).
agent_(alice_and_bob_joint_return_2019,bob_s7703_b_1_neg).
start_(alice_and_bob_joint_return_2019,d2019_01_01).
end_(alice_and_bob_joint_return_2019,d2019_12_31).

% Test
:- \+ s7703_b_1(alice_s7703_b_1_neg,alice_s_house_s7703_b_1_neg,charlie_s7703_b_1_neg,2018).
:- halt.
% Text
% Alice and Bob got married on April 5th, 2012. Alice and Bob have a son, Charlie, who was born on September 16th, 2017. Alice and Charlie live in a home maintained by Alice since September 16th, 2017. Alice is entitled to a deduction for Charlie under section 151(c) for the years 2017 to 2019. Alice files a separate return.

% Question
% Section 7703(b)(1) applies to Alice for the year 2018. Entailment

% Facts
person(alice_s7703_b_1_pos).
person(bob_s7703_b_1_pos).
person(charlie_s7703_b_1_pos).

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

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

household(alice_s_house_s7703_b_1_pos).
finance(1).

marriage_(alice_and_bob_s7703_b_1_pos).
agent_(alice_and_bob_s7703_b_1_pos,alice_s7703_b_1_pos).
agent_(alice_and_bob_s7703_b_1_pos,bob_s7703_b_1_pos).
start_(alice_and_bob_s7703_b_1_pos,d2012_04_05).
son_(charlie_is_born_s7703_b_1_pos).
agent_(charlie_is_born_s7703_b_1_pos,charlie_s7703_b_1_pos).
patient_(charlie_is_born_s7703_b_1_pos,bob_s7703_b_1_pos).
patient_(charlie_is_born_s7703_b_1_pos,alice_s7703_b_1_pos).
start_(charlie_is_born_s7703_b_1_pos,d2017_09_16).
residence_(alice_residence_s7703_b_1_pos).
agent_(alice_residence_s7703_b_1_pos,alice_s7703_b_1_pos).
patient_(alice_residence_s7703_b_1_pos,alice_s_house_s7703_b_1_pos).
start_(alice_residence_s7703_b_1_pos,d2017_09_16).
residence_(charlie_residence_s7703_b_1_pos).
agent_(charlie_residence_s7703_b_1_pos,charlie_s7703_b_1_pos).
patient_(charlie_residence_s7703_b_1_pos,alice_s_house_s7703_b_1_pos).
start_(charlie_residence_s7703_b_1_pos,d2017_09_16).

% NOTE: should be generated to 2117 + dates should be validated
alice_household_maintenance(2017,'alice_maintains_household_s7703_b_1_pos2017',d2017_09_16,"2017-12-31").
alice_household_maintenance(2018,'alice_maintains_household_s7703_b_1_pos2018',d2018_01_01,"2018-12-31").
alice_household_maintenance(2019,'alice_maintains_household_s7703_b_1_pos2019',d2019_01_01,"2019-12-31").
alice_household_maintenance(2020,'alice_maintains_household_s7703_b_1_pos2020',d2020_01_01,"2020-12-31").
alice_household_maintenance(2021,'alice_maintains_household_s7703_b_1_pos2021',d2021_01_01,"2021-12-31").
alice_household_maintenance(2022,'alice_maintains_household_s7703_b_1_pos2022',d2022_01_01,"2022-12-31").
alice_household_maintenance(2023,'alice_maintains_household_s7703_b_1_pos2023',d2023_01_01,"2023-12-31").
alice_household_maintenance(2024,'alice_maintains_household_s7703_b_1_pos2024',d2024_01_01,"2024-12-31").
alice_household_maintenance(2025,'alice_maintains_household_s7703_b_1_pos2025',d2025_01_01,"2025-12-31").
alice_household_maintenance(2026,'alice_maintains_household_s7703_b_1_pos2026',d2026_01_01,"2026-12-31").
alice_household_maintenance(2027,'alice_maintains_household_s7703_b_1_pos2027',d2027_01_01,"2027-12-31").
alice_household_maintenance(2028,'alice_maintains_household_s7703_b_1_pos2028',d2028_01_01,"2028-12-31").
alice_household_maintenance(2029,'alice_maintains_household_s7703_b_1_pos2029',d2029_01_01,"2029-12-31").
alice_household_maintenance(2030,'alice_maintains_household_s7703_b_1_pos2030',d2030_01_01,"2030-12-31").
alice_household_maintenance(2031,'alice_maintains_household_s7703_b_1_pos2031',d2031_01_01,"2031-12-31").
alice_household_maintenance(2032,'alice_maintains_household_s7703_b_1_pos2032',d2032_01_01,"2032-12-31").
alice_household_maintenance(2033,'alice_maintains_household_s7703_b_1_pos2033',d2033_01_01,"2033-12-31").
alice_household_maintenance(2034,'alice_maintains_household_s7703_b_1_pos2034',d2034_01_01,"2034-12-31").
alice_household_maintenance(2035,'alice_maintains_household_s7703_b_1_pos2035',d2035_01_01,"2035-12-31").
alice_household_maintenance(2036,'alice_maintains_household_s7703_b_1_pos2036',d2036_01_01,"2036-12-31").
alice_household_maintenance(2037,'alice_maintains_household_s7703_b_1_pos2037',d2037_01_01,"2037-12-31").
alice_household_maintenance(2038,'alice_maintains_household_s7703_b_1_pos2038',d2038_01_01,"2038-12-31").
alice_household_maintenance(2039,'alice_maintains_household_s7703_b_1_pos2039',d2039_01_01,"2039-12-31").
alice_household_maintenance(2040,'alice_maintains_household_s7703_b_1_pos2040',d2040_01_01,"2040-12-31").
alice_household_maintenance(2041,'alice_maintains_household_s7703_b_1_pos2041',d2041_01_01,"2041-12-31").
alice_household_maintenance(2042,'alice_maintains_household_s7703_b_1_pos2042',d2042_01_01,"2042-12-31").
alice_household_maintenance(2043,'alice_maintains_household_s7703_b_1_pos2043',d2043_01_01,"2043-12-31").
alice_household_maintenance(2044,'alice_maintains_household_s7703_b_1_pos2044',d2044_01_01,"2044-12-31").
alice_household_maintenance(2045,'alice_maintains_household_s7703_b_1_pos2045',d2045_01_01,"2045-12-31").
alice_household_maintenance(2046,'alice_maintains_household_s7703_b_1_pos2046',d2046_01_01,"2046-12-31").
alice_household_maintenance(2047,'alice_maintains_household_s7703_b_1_pos2047',d2047_01_01,"2047-12-31").
alice_household_maintenance(2048,'alice_maintains_household_s7703_b_1_pos2048',d2048_01_01,"2048-12-31").
alice_household_maintenance(2049,'alice_maintains_household_s7703_b_1_pos2049',d2049_01_01,"2049-12-31").
alice_household_maintenance(2050,'alice_maintains_household_s7703_b_1_pos2050',d2050_01_01,"2050-12-31").
% alice_household_maintenance(Year,Event,Start_day,End_day) :-
%     between(2017,2117,Year), % avoid infinite forward loop
%     atom_concat('alice_maintains_household_',Year,Event),
%     (((Year==2017)->(Start_day=d2017_09_16));first_day_year(Year,Start_day)),
%     last_day_year(Year,End_day).
payment_(Event) :- alice_household_maintenance(_,Event,_,_).
agent_(Event,alice_s7703_b_1_pos) :- alice_household_maintenance(_,Event,_,_).
amount_(Event,1) :- alice_household_maintenance(_,Event,_,_).
purpose_(Event,alice_s_house_s7703_b_1_pos) :- alice_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- alice_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- alice_household_maintenance(_,Event,_,End_day).
s151_c_applies(alice_s7703_b_1_pos,charlie_s7703_b_1_pos,Year) :- between(2017,2019,Year).

% Test
:- s7703_b_1(alice_s7703_b_1_pos,alice_s_house_s7703_b_1_pos,charlie_s7703_b_1_pos,2018).
:- halt.
% Text
% Alice and Bob got married on April 5th, 2012. Alice and Bob have a son, Charlie, who was born on September 16th, 2017. Alice and Charlie live in a home maintained by Alice since September 16th, 2017. Alice is entitled to a deduction for Charlie under section 151(c) for the years 2017 to 2019. Bob lived in the same house as Alice and Charlie from September 16th, 2017 until October 10th, 2018.

% Question
% Section 7703(b)(3) applies to Alice maintaining her home for the year 2018. Contradiction

% Facts
person(alice_s7703_b_3_neg).
person(bob_s7703_b_3_neg).
person(charlie_s7703_b_3_neg).

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
date(d2018_10_10).
date_split(d2018_10_10, 2018, 10, 10).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

household(alice_s_house_s7703_b_3_neg).
finance(1).

marriage_(alice_and_bob_s7703_b_3_neg).
agent_(alice_and_bob_s7703_b_3_neg,alice_s7703_b_3_neg).
agent_(alice_and_bob_s7703_b_3_neg,bob_s7703_b_3_neg).
start_(alice_and_bob_s7703_b_3_neg,d2012_04_05).
son_(charlie_is_born_s7703_b_3_neg).
agent_(charlie_is_born_s7703_b_3_neg,charlie_s7703_b_3_neg).
patient_(charlie_is_born_s7703_b_3_neg,bob_s7703_b_3_neg).
patient_(charlie_is_born_s7703_b_3_neg,alice_s7703_b_3_neg).
start_(charlie_is_born_s7703_b_3_neg,d2017_09_16).
residence_(home_s7703_b_3_neg).
agent_(home_s7703_b_3_neg,alice_s7703_b_3_neg).
agent_(home_s7703_b_3_neg,charlie_s7703_b_3_neg).
patient_(home_s7703_b_3_neg,alice_s_house_s7703_b_3_neg).
start_(home_s7703_b_3_neg,d2017_09_16).

% NOTE: should be generated to 2117 + dates should be validated
alice_household_maintenance(2017,'alice_maintains_household_s7703_b_3_neg2017',d2017_09_16,"2017-12-31").
alice_household_maintenance(2018,'alice_maintains_household_s7703_b_3_neg2018',d2018_01_01,"2018-12-31").
alice_household_maintenance(2019,'alice_maintains_household_s7703_b_3_neg2019',d2019_01_01,"2019-12-31").
alice_household_maintenance(2020,'alice_maintains_household_s7703_b_3_neg2020',d2020_01_01,"2020-12-31").
alice_household_maintenance(2021,'alice_maintains_household_s7703_b_3_neg2021',d2021_01_01,"2021-12-31").
alice_household_maintenance(2022,'alice_maintains_household_s7703_b_3_neg2022',d2022_01_01,"2022-12-31").
alice_household_maintenance(2023,'alice_maintains_household_s7703_b_3_neg2023',d2023_01_01,"2023-12-31").
alice_household_maintenance(2024,'alice_maintains_household_s7703_b_3_neg2024',d2024_01_01,"2024-12-31").
alice_household_maintenance(2025,'alice_maintains_household_s7703_b_3_neg2025',d2025_01_01,"2025-12-31").
alice_household_maintenance(2026,'alice_maintains_household_s7703_b_3_neg2026',d2026_01_01,"2026-12-31").
alice_household_maintenance(2027,'alice_maintains_household_s7703_b_3_neg2027',d2027_01_01,"2027-12-31").
alice_household_maintenance(2028,'alice_maintains_household_s7703_b_3_neg2028',d2028_01_01,"2028-12-31").
alice_household_maintenance(2029,'alice_maintains_household_s7703_b_3_neg2029',d2029_01_01,"2029-12-31").
alice_household_maintenance(2030,'alice_maintains_household_s7703_b_3_neg2030',d2030_01_01,"2030-12-31").
alice_household_maintenance(2031,'alice_maintains_household_s7703_b_3_neg2031',d2031_01_01,"2031-12-31").
alice_household_maintenance(2032,'alice_maintains_household_s7703_b_3_neg2032',d2032_01_01,"2032-12-31").
alice_household_maintenance(2033,'alice_maintains_household_s7703_b_3_neg2033',d2033_01_01,"2033-12-31").
alice_household_maintenance(2034,'alice_maintains_household_s7703_b_3_neg2034',d2034_01_01,"2034-12-31").
alice_household_maintenance(2035,'alice_maintains_household_s7703_b_3_neg2035',d2035_01_01,"2035-12-31").
alice_household_maintenance(2036,'alice_maintains_household_s7703_b_3_neg2036',d2036_01_01,"2036-12-31").
alice_household_maintenance(2037,'alice_maintains_household_s7703_b_3_neg2037',d2037_01_01,"2037-12-31").
alice_household_maintenance(2038,'alice_maintains_household_s7703_b_3_neg2038',d2038_01_01,"2038-12-31").
alice_household_maintenance(2039,'alice_maintains_household_s7703_b_3_neg2039',d2039_01_01,"2039-12-31").
alice_household_maintenance(2040,'alice_maintains_household_s7703_b_3_neg2040',d2040_01_01,"2040-12-31").
alice_household_maintenance(2041,'alice_maintains_household_s7703_b_3_neg2041',d2041_01_01,"2041-12-31").
alice_household_maintenance(2042,'alice_maintains_household_s7703_b_3_neg2042',d2042_01_01,"2042-12-31").
alice_household_maintenance(2043,'alice_maintains_household_s7703_b_3_neg2043',d2043_01_01,"2043-12-31").
alice_household_maintenance(2044,'alice_maintains_household_s7703_b_3_neg2044',d2044_01_01,"2044-12-31").
alice_household_maintenance(2045,'alice_maintains_household_s7703_b_3_neg2045',d2045_01_01,"2045-12-31").
alice_household_maintenance(2046,'alice_maintains_household_s7703_b_3_neg2046',d2046_01_01,"2046-12-31").
alice_household_maintenance(2047,'alice_maintains_household_s7703_b_3_neg2047',d2047_01_01,"2047-12-31").
alice_household_maintenance(2048,'alice_maintains_household_s7703_b_3_neg2048',d2048_01_01,"2048-12-31").
alice_household_maintenance(2049,'alice_maintains_household_s7703_b_3_neg2049',d2049_01_01,"2049-12-31").
alice_household_maintenance(2050,'alice_maintains_household_s7703_b_3_neg2050',d2050_01_01,"2050-12-31").
% alice_household_maintenance(Year,Event,Start_day,End_day) :-
%     between(2017,2117,Year), % avoid infinite forward loop
%     atom_concat('alice_maintains_household_',Year,Event),
%     (((Year==2017)->(Start_day=d2017_09_16));first_day_year(Year,Start_day)),
%     last_day_year(Year,End_day).

payment_(Event) :- alice_household_maintenance(_,Event,_,_).
agent_(Event,alice_s7703_b_3_neg) :- alice_household_maintenance(_,Event,_,_).
amount_(Event,1) :- alice_household_maintenance(_,Event,_,_).
purpose_(Event,home_s7703_b_3_neg) :- alice_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- alice_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- alice_household_maintenance(_,Event,_,End_day).
s151_c_applies(alice_s7703_b_3_neg,charlie_s7703_b_3_neg,Year) :- between(2017,2019,Year).
residence_(bob_lives_alice_house_s7703_b_3_neg).
agent_(bob_lives_alice_house_s7703_b_3_neg,bob_s7703_b_3_neg).
patient_(bob_lives_alice_house_s7703_b_3_neg,alice_s_house_s7703_b_3_neg).
start_(bob_lives_alice_house_s7703_b_3_neg,d2017_09_16).
end_(bob_lives_alice_house_s7703_b_3_neg,d2018_10_10).

% Test
:- \+ s7703_b_3(alice_s7703_b_3_neg,bob_s7703_b_3_neg,alice_s_house_s7703_b_3_neg,2018).
:- halt.
% Text
% Alice and Bob got married on April 5th, 2012. Alice and Bob have a son, Charlie, who was born on September 16th, 2017. Alice and Charlie live in a home maintained by Alice since September 16th, 2017. Alice is entitled to a deduction for Charlie under section 151(c) for the years 2017 to 2019. Bob lived in the same house as Alice and Charlie from September 16th, 2017 until February 10th, 2018.

% Question
% Section 7703(b)(3) applies to Alice maintaining her home for the year 2018. Entailment

% Facts
person(alice_s7703_b_3_pos).
person(bob_s7703_b_3_pos).
person(charlie_s7703_b_3_pos).

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
date(d2018_02_10).
date_split(d2018_02_10, 2018, 2, 10).
date(d2018_12_31).
date_split(d2018_12_31, 2018, 12, 31).

year(2019).
date(d2019_01_01).
date_split(d2019_01_01, 2019, 1, 1).
date(d2019_12_31).
date_split(d2019_12_31, 2019, 12, 31).

household(alice_s_house_s7703_b_3_pos).
finance(1).

marriage_(alice_and_bob_s7703_b_3_pos).
agent_(alice_and_bob_s7703_b_3_pos,alice_s7703_b_3_pos).
agent_(alice_and_bob_s7703_b_3_pos,bob_s7703_b_3_pos).
start_(alice_and_bob_s7703_b_3_pos,d2012_04_05).
son_(charlie_is_born_s7703_b_3_pos).
agent_(charlie_is_born_s7703_b_3_pos,charlie_s7703_b_3_pos).
patient_(charlie_is_born_s7703_b_3_pos,bob_s7703_b_3_pos).
patient_(charlie_is_born_s7703_b_3_pos,alice_s7703_b_3_pos).
start_(charlie_is_born_s7703_b_3_pos,d2017_09_16).
residence_(home_s7703_b_3_pos).
agent_(home_s7703_b_3_pos,alice_s7703_b_3_pos).
agent_(home_s7703_b_3_pos,charlie_s7703_b_3_pos).
patient_(home_s7703_b_3_pos,alice_s_house_s7703_b_3_pos).
start_(home_s7703_b_3_pos,d2017_09_16).

% NOTE: should be generated to 2117 + dates should be validated
alice_household_maintenance(2017,'alice_maintains_household_s7703_b_3_pos2017',d2017_09_16,"2017-12-31").
alice_household_maintenance(2018,'alice_maintains_household_s7703_b_3_pos2018',d2018_01_01,"2018-12-31").
alice_household_maintenance(2019,'alice_maintains_household_s7703_b_3_pos2019',d2019_01_01,"2019-12-31").
alice_household_maintenance(2020,'alice_maintains_household_s7703_b_3_pos2020',d2020_01_01,"2020-12-31").
alice_household_maintenance(2021,'alice_maintains_household_s7703_b_3_pos2021',d2021_01_01,"2021-12-31").
alice_household_maintenance(2022,'alice_maintains_household_s7703_b_3_pos2022',d2022_01_01,"2022-12-31").
alice_household_maintenance(2023,'alice_maintains_household_s7703_b_3_pos2023',d2023_01_01,"2023-12-31").
alice_household_maintenance(2024,'alice_maintains_household_s7703_b_3_pos2024',d2024_01_01,"2024-12-31").
alice_household_maintenance(2025,'alice_maintains_household_s7703_b_3_pos2025',d2025_01_01,"2025-12-31").
alice_household_maintenance(2026,'alice_maintains_household_s7703_b_3_pos2026',d2026_01_01,"2026-12-31").
alice_household_maintenance(2027,'alice_maintains_household_s7703_b_3_pos2027',d2027_01_01,"2027-12-31").
alice_household_maintenance(2028,'alice_maintains_household_s7703_b_3_pos2028',d2028_01_01,"2028-12-31").
alice_household_maintenance(2029,'alice_maintains_household_s7703_b_3_pos2029',d2029_01_01,"2029-12-31").
alice_household_maintenance(2030,'alice_maintains_household_s7703_b_3_pos2030',d2030_01_01,"2030-12-31").
alice_household_maintenance(2031,'alice_maintains_household_s7703_b_3_pos2031',d2031_01_01,"2031-12-31").
alice_household_maintenance(2032,'alice_maintains_household_s7703_b_3_pos2032',d2032_01_01,"2032-12-31").
alice_household_maintenance(2033,'alice_maintains_household_s7703_b_3_pos2033',d2033_01_01,"2033-12-31").
alice_household_maintenance(2034,'alice_maintains_household_s7703_b_3_pos2034',d2034_01_01,"2034-12-31").
alice_household_maintenance(2035,'alice_maintains_household_s7703_b_3_pos2035',d2035_01_01,"2035-12-31").
alice_household_maintenance(2036,'alice_maintains_household_s7703_b_3_pos2036',d2036_01_01,"2036-12-31").
alice_household_maintenance(2037,'alice_maintains_household_s7703_b_3_pos2037',d2037_01_01,"2037-12-31").
alice_household_maintenance(2038,'alice_maintains_household_s7703_b_3_pos2038',d2038_01_01,"2038-12-31").
alice_household_maintenance(2039,'alice_maintains_household_s7703_b_3_pos2039',d2039_01_01,"2039-12-31").
alice_household_maintenance(2040,'alice_maintains_household_s7703_b_3_pos2040',d2040_01_01,"2040-12-31").
alice_household_maintenance(2041,'alice_maintains_household_s7703_b_3_pos2041',d2041_01_01,"2041-12-31").
alice_household_maintenance(2042,'alice_maintains_household_s7703_b_3_pos2042',d2042_01_01,"2042-12-31").
alice_household_maintenance(2043,'alice_maintains_household_s7703_b_3_pos2043',d2043_01_01,"2043-12-31").
alice_household_maintenance(2044,'alice_maintains_household_s7703_b_3_pos2044',d2044_01_01,"2044-12-31").
alice_household_maintenance(2045,'alice_maintains_household_s7703_b_3_pos2045',d2045_01_01,"2045-12-31").
alice_household_maintenance(2046,'alice_maintains_household_s7703_b_3_pos2046',d2046_01_01,"2046-12-31").
alice_household_maintenance(2047,'alice_maintains_household_s7703_b_3_pos2047',d2047_01_01,"2047-12-31").
alice_household_maintenance(2048,'alice_maintains_household_s7703_b_3_pos2048',d2048_01_01,"2048-12-31").
alice_household_maintenance(2049,'alice_maintains_household_s7703_b_3_pos2049',d2049_01_01,"2049-12-31").
alice_household_maintenance(2050,'alice_maintains_household_s7703_b_3_pos2050',d2050_01_01,"2050-12-31").
% alice_household_maintenance(Year,Event,Start_day,End_day) :-
%     between(2017,2117,Year), % avoid infinite forward loop
%     atom_concat('alice_maintains_household_',Year,Event),
%     (((Year==2017)->(Start_day=d2017_09_16));first_day_year(Year,Start_day)),
%     last_day_year(Year,End_day).

payment_(Event) :- alice_household_maintenance(_,Event,_,_).
agent_(Event,alice_s7703_b_3_pos) :- alice_household_maintenance(_,Event,_,_).
amount_(Event,1) :- alice_household_maintenance(_,Event,_,_).
purpose_(Event,home_s7703_b_3_pos) :- alice_household_maintenance(_,Event,_,_).
start_(Event,Start_day) :- alice_household_maintenance(_,Event,Start_day,_).
end_(Event,End_day) :- alice_household_maintenance(_,Event,_,End_day).
s151_c_applies(alice_s7703_b_3_pos,charlie_s7703_b_3_pos,Year) :- between(2017,2019,Year).
residence_(bob_lives_alice_house_s7703_b_3_pos).
agent_(bob_lives_alice_house_s7703_b_3_pos,bob_s7703_b_3_pos).
patient_(bob_lives_alice_house_s7703_b_3_pos,alice_s_house_s7703_b_3_pos).
start_(bob_lives_alice_house_s7703_b_3_pos,d2017_09_16).
end_(bob_lives_alice_house_s7703_b_3_pos,d2018_02_10).

% Test
:- s7703_b_3(alice_s7703_b_3_pos,bob_s7703_b_3_pos,alice_s_house_s7703_b_3_pos,2018).
:- halt.

END OF EXAMPLES

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

llm_manager.chat_completion(prompt,print_result=True)
#!/usr/bin/env python3

import random

data = [
["What does the Constitution do?", ["sets up the government", "defines the government", "protects basic rights of Americans"]],
["What is an amendment?", ["a change to the Constitution", "an addition to the Constitution"]],
["What is one right or freedom from the First Amendment?", ["speech", "religion", "assembly", "press", "petition the government"]],
["What did the Declaration of Independence do?", ["announced our independence from Great Britain", "declared our independence (from Great Britain)", "said that the United States is free from Great Britain"]],
["What are two rights in the Declaration of Independence?", ["life", "liberty", "pursuit of happiness"]],
["Who makes federal laws?", ["Congress", "Senate and House of Representatives", "legislature"]],
["Who is one of your state’s U.S. Senators now?", ["Kamala Harris", "Dianne Feinstein"]],
["The House of Representatives has how many voting members?", ["four hundred thirty-five"]],
["Name your U.S. Representative", ["Katie Porter"]],
["Who does a U.S. Senator represent?", ["all people of the state"]],
["In what month do we vote for President?", ["November"]],
["Who is the Chief Justice of the United States now?", ["John Roberts"]],
["Who is the Governor of your state now?", ["Gavin Newsom"]],
["What is the name of the Speaker of the House of Representatives now?", ["Nancy Pelosi"]],
["If both the President and the Vice President can no longer serve, who becomes President?", ["the Speaker of the House"]],
["What are two Cabinet-level positions?", ["Secretary of Agriculture", "Secretary of Commerce", "Secretary of Defense", "Secretary of State", "Attorney General", "Vice President"]],
["What does the judicial branch do?", ["reviews laws", "explains laws", "resolves disputes", "decides if a law goes against the Constitution"]],
["Under our Constitution, some powers belong to the federal government. What is one power of the federal government?", ["to print money", "to declare war", "to make treaties"]],
["Under our Constitution, some powers belong to the states. What is one power of the states?", ["provide schooling and education", "provide protection", "provide safety", "give a driver’s license", "approve zoning and land use"]],
["What is the capital of your state?", ["Sacramento"]],
["There are four amendments to the Constitution about who can vote. Describe one of them.", ["Citizens eighteen and older can vote", "You don’t have to pay a poll tax to vote", "Women and men can vote", "A male citizen of any race can vote"]],
["What is one responsibility that is only for United States citizens?", ["serve on a jury", "vote in a federal election"]],
["Name one right only for United States citizens", ["vote in a federal election", "run for federal office"]],
["What are two rights of everyone living in the United States?", ["freedom of expression", "freedom of speech", "freedom of assembly", "freedom to petition the government", "freedom of religion", "the right to bear arms"]],
["What do we show loyalty to when we say the Pledge of Allegiance?", ["the United States", "the flag"]],
["What is one promise you make when you become a United States citizen?", ["give up loyalty to other countries", "defend the Constitution and laws of the United States", "obey the laws of the United States", "serve in the U.S. military if needed", "serve the nation if needed", "be loyal to the United States"]],
["What are two ways that Americans can participate in their democracy?", ["vote", "join a political party", "help with a campaign", "join a civic group", "join a community group", "give an elected official your opinion on an issue", "call Senators and Representatives", "publicly support or oppose an issue or policy", "run for office", "write to a newspaper"]],
["When must all men register for the Selective Service?", ["at age eighteen", "between eighteen and twenty-six"]],
["Why did the colonists fight the British?", ["because of high taxes", "because the British army stayed in their houses", "because they didn’t have self-government"]],
["Who wrote the Declaration of Independence?", ["Thomas Jefferson"]],
["When was the Declaration of Independence adopted?", ["July 4, 1776"]],
["There were 13 original states. Name three", ["New Hampshire", "Massachusetts", "Rhode Island", "Connecticut", "New York", "New Jersey", "Pennsylvania", "Delaware", "Maryland", "Virginia", "North Carolina", "South Carolina", "Georgia"]],
["What happened at the Constitutional Convention?", ["The Constitution was written", "The Founding Fathers wrote the Constitution"]],
["When was the Constitution written?", ["1787"]],
["The Federalist Papers supported the passage of the U.S. Constitution. Name one of the writers.", ["James Madison", "Alexander Hamilton", "John Jay", "Publius"]],
["What is one thing Benjamin Franklin is famous for?", ["U.S. diplomat", "oldest member of the Constitutional Convention", "first Postmaster General of the United States", "writer of Poor Richard’s Almanac", "started the first free libraries"]],
["Who is the “Father of Our Country”?", ["George Washington"]],
["Who was the first President?", ["George Washington"]],
["Name one problem that led to the Civil War.", ["slavery", "economic reasons", "states’ rights"]],
["What was one important thing that Abraham Lincoln did?", ["freed the slaves", " saved the Union", "led the United States during the Civil War"]],
["What did the Emancipation Proclamation do?", ["freed the slaves", "freed slaves in the Confederacy"]],
["What did Susan B. Anthony do?", ["fought for women’s rights", "fought for civil rights"]],
["Who was President during World War I?", ["Woodrow Wilson"]],
["Who was President during the Great Depression and World War II?", ["Franklin Roosevelt"]],
["Who did the United States fight in World War II?", ["Japan, Germany, and Italy"]],
["What movement tried to end racial discrimination?", ["civil rights"]],
["What did Martin Luther King, Jr. do?", ["fought for civil rights", "worked for equality for all Americans"]],
["What major event happened on September 11, 2001, in the United States?", ["Terrorists attacked the United States."]],
["Name one U.S. territory", ["Puerto Rico", "U.S. Virgin Islands", "American Samoa", "Northern Mariana Islands", "Guam"]],
["Where is the Statue of Liberty?", ["New York", "Liberty Island", "on the Hudson"]],
["What is the name of the national anthem?", ["The Star-Spangled Banner"]],
]

def preprocess(s):
    result = set()
    for p in s.split():
        p = p.lower()
        if p == "a":
            continue
        if p == "the":
            continue
        result.add(p)
    return result

def eq(a, ans):
    return preprocess(a) == preprocess(ans)

ok = 0
N = 10
asked = set()
for i in range(N):
    i_q = random.randrange(len(data))
    while i_q in asked:
        i_q = random.randrange(len(data))
    asked.add(i_q)
    q = data[i_q]
    print(q[0])
    answer = input()
    q_ok = False
    for a in q[1]:
        if eq(a, answer):
            q_ok = True
    if q_ok:
        print("ok")
        ok += 1
    else:
        print("wrong:\n%s" % ("\n".join(q[1])))
    print("%d/%d" % (ok, i + 1))
print("%d/%d" % (ok, N))

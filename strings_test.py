#!python

from strings import contains, find_index, find_all_indexes
import unittest


class StringsTest(unittest.TestCase):

    def test_contains_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert contains('abc', '') is True  # all strings contain empty string
        assert contains('abc', 'a') is True  # single letters are easy
        assert contains('abc', 'b') is True
        assert contains('abc', 'c') is True
        assert contains('abc', 'ab') is True  # multiple letters are harder
        assert contains('abc', 'bc') is True
        assert contains('abc', 'abc') is True  # all strings contain themselves
        assert contains('aaa', 'a') is True  # multiple occurrences
        assert contains('aaa', 'aa') is True  # overlapping pattern
        # TODO: Write more positive test cases with assert is True statements
        # ...

    def test_contains_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert contains('abc', 'z') is False  # remember to test other letters
        assert contains('abc', 'ac') is False  # important to test close cases
        assert contains('abc', 'az') is False  # first letter, but not last
        assert contains('abc', 'abz') is False  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is False statements
        # ...

    def test_contains_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert contains('ababc', 'ab') is True  # multiple occurrences
        assert contains('banana', 'na') is True  # multiple occurrences
        assert contains('ababc', 'abc') is True  # overlapping prefix
        assert contains('bananas', 'nas') is True  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        # ...

    def test_find_index_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_index('abc', '') == 0  # all strings contain empty string
        assert find_index('abc', 'a') == 0  # single letters are easy
        assert find_index('abc', 'b') == 1
        assert find_index('abc', 'c') == 2
        assert find_index('abc', 'ab') == 0  # multiple letters are harder
        assert find_index('abc', 'bc') == 1
        assert find_index('abc', 'abc') == 0  # all strings contain themselves
        assert find_index('aaa', 'a') == 0  # multiple occurrences
        assert find_index('aaa', 'aa') == 0  # overlapping pattern
        # TODO: Write more positive test cases with assert equal int statements
        # ...

    def test_find_index_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_index('abc', 'z') is None  # remember to test other letters
        assert find_index('abc', 'ac') is None  # important to test close cases
        assert find_index('abc', 'az') is None  # first letter, but not last
        assert find_index('abc', 'abz') is None  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is None statements
        # ...

    def test_find_index_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_index('ababc', 'abc') == 2  # overlapping prefix
        assert find_index('bananas', 'nas') == 4  # overlapping prefix
        assert find_index('abcabcabc', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcab', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcdef', 'abcd') == 3  # overlapping prefix
        assert find_index('abcabcdef', 'abcdef') == 3  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcde') == 7  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcd') == 3  # multiple occurrences, overlapping prefix
        assert find_index('abra cadabra', 'abra') == 0  # multiple occurrences
        assert find_index('abra cadabra', 'adab') == 6  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        # ...

    def test_find_all_indexes_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_all_indexes('abc', '') == [0, 1, 2]  # all strings contain empty string
        assert find_all_indexes('abc', 'a') == [0]  # single letters are easy
        assert find_all_indexes('abc', 'b') == [1]
        assert find_all_indexes('abc', 'c') == [2]
        assert find_all_indexes('abc', 'ab') == [0]  # multiple letters are harder
        assert find_all_indexes('abc', 'bc') == [1]
        assert find_all_indexes('abc', 'abc') == [0]  # all strings contain themselves
        assert find_all_indexes('aaa', 'a') == [0, 1, 2]  # multiple occurrences
        assert find_all_indexes('aaa', 'aa') == [0, 1]  # overlapping pattern
        # TODO: Write more positive test cases with assert equal list statements
        # ...

    def test_find_all_indexes_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_all_indexes('abc', 'z') == []  # remember to test other letters
        assert find_all_indexes('abc', 'ac') == []  # important to test close cases
        assert find_all_indexes('abc', 'az') == []  # first letter, but not last
        assert find_all_indexes('abc', 'abz') == []  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert equal list statements
        # ...

    def test_find_all_indexes_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_all_indexes('ababc', 'abc') == [2]  # overlapping prefix
        assert find_all_indexes('bananas', 'nas') == [4]  # overlapping prefix
        assert find_all_indexes('abcabcabc', 'abc') == [0, 3, 6]  # multiple occurrences
        assert find_all_indexes('abcabcab', 'abc') == [0, 3]  # multiple occurrences
        assert find_all_indexes('abcabcdef', 'abcd') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdef', 'abcdef') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcde') == [7]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcd') == [3, 7]  # multiple occurrences, overlapping prefix
        assert find_all_indexes('abra cadabra', 'abra') == [0, 8]  # multiple occurrences
        assert find_all_indexes('abra cadabra', 'adab') == [6]  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        # ...

    def test_walk_the_gauntlet(self):
        # METAL AF
        assert find_all_indexes('99 Red Balloons', '99') == [0]
        assert find_all_indexes('99 Red Balloons', '99 RED BALLOONS') == []
        assert find_all_indexes('sidyuf87723yh4j23!@#(@!$HRJWEfekwf', '@') == [18, 21]
        assert find_all_indexes('Marlene Dietrich', 'Backpfeifengesicht') == []
        assert find_all_indexes('anananananananananananananananananan', 'anana') == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        assert find_all_indexes('施氏食獅史', '食') == [2]
        assert find_all_indexes('''
            Donald J. Trump
            @realDonaldTrump

            Despite the negative press covfefe

            Retweets Likes
            11,029 13,430
            12:06 AM - 31 May 2017
            ''',
            'covfefe') == [98]
        assert find_all_indexes('''
            To be fair, you have to have a very high IQ to understand Rick and Morty. 
            The humor is extremely subtle, and without a solid grasp of theoretical physics 
            most of the jokes will go over a typical viewer's head. There's also Rick's nihilistic 
            outlook, which is deftly woven into his characterisation - his personal philosophy 
            draws heavily from Narodnaya Volya literature, for instance. The fans understand this 
            stuff; they have the intellectual capacity to truly appreciate the depths of these jokes, 
            to realize that they're not just funny- they say something deep about LIFE. As a 
            consequence people who dislike Rick and Morty truly ARE idiots- of course they wouldn't 
            appreciate, for instance, the humour in Rick's existential catchphrase "Wubba Lubba Dub 
            Dub," which itself is a cryptic reference to Turgenev's Russian epic Fathers and Sons. 
            I'm smirking right now just imagining one of those addlepated simpletons scratching their 
            heads in confusion as Dan Harmon's genius unfolds itself on their television screens. 
            What fools... how I pity them. 😂 And yes by the way, I DO have a Rick and Morty tattoo. 
            And no, you cannot see it. It's for the ladies' eyes only- And even they have to 
            demonstrate that they're within 5 IQ points of my own (preferably lower) beforehand.
            ''',
            'Morty') == [80, 725, 1263]
        assert find_all_indexes('''
            T̜͔̱ọ̺̺̝̤ ̥̞̩͓̜i͔̪̖͔̭̯͟n͓̬̤̯̖v̤ͅo̡̤̺̙͇̳͈̭k͕̭e̪̬͍̭̰͝ͅ ̵̹t͓̣̞̲͞h͉̰̥͎͢e͎̳͇͡ ͈̰͈̭̹͕̥h͍̜̬i̞̯͚͔̼̯v̭͚͙̻̙͟e̡͍̩̩̗͉-̟͕̖͓͚͓́m̙ͅi̭̭̮̦͖̫n̪̭͇d̮̲̖̤͓͟ ҉͍̰̗̹̯r̼̪͕͡e͠pr̷e͉͉̲̖s͉͙é̠̗̰̹n̡̝͎t͖̼̯͖̱͉in͓͔̝͍̞͉͜g̬̬̣ ͎̳̦͔̹̟̟c͉̺̮h̫̞͈̘̯̀a̼o̷̟̟̣̪s̝̕.̴̝̣͉͉͎̺
            ̫̀I̝͖̣͎͇̲͠ͅn̲̪̦v̸̫̣̖̪̺̙o̸̠͙͍̩k̜i̜n̳̭̖̼ͅg̢ ̀t̰͙h̯͙͇̬͖̟e̟̭̘̱̟̦ ̩͉̗̱̰̝͡f͕̙̲̲͟ͅͅee̙̜͈͖l̵̙͙i̩͕̮̳͙̙̝n͕g̡̻̥̲̞̰̝̟ ̰o͖͎f̛ ͈̳c̩̟̱͈̦͘ͅh̝̮a̘̺͈o͚̲̯̞͕s̘̞̝̹̗͇͈͞.̡͓̪̮̪
            ͕̻͈̻͕͉̀W̼̗̺̫̞͖it̠̦͎̪͓̺̻́h̭̼̘͕͔͔ ͕͓̠̟̙͉̩o̪͇̲̯u̸̟͚̰̠̲ṯ̖̭ ̰̣̣o̫̣̤͖̫͚͞ͅr̻d͏̘̣͙͓̫̭̩e̴̹͙͎̟r̹.
            ̝̤̩́The ͉̜̟͈͍N̯̤̞͔e̦̹̯̠̥̹z̡͇̭p̪̱̳ę̟̙͙ŕ̦͓̤͉͙̗͈d̴̖̖̺̩̼i̷̼̩a̺̲̪̘n҉̲̣ ͎̩̜h̬̗͉̱͉͈i̻͉̘̹̕v̴͉̤̱̖è̝̭̯̣̘-͇̘͔̜̜̜͞ͅm̵̠̝̦i̠̣͔n͖͈d҉̲̺ ̡̖͇͍o͘f̵ ch̩̞̗̱̘̀a̵̗̤͈̟̭o҉s.̸ ̠̞̠̭͖̦Z͘a͕̣̪̫͇̙l̗͖̳g͎̟̻o͖͚̮̬͘.̴̩
            ͔̝̦͖̬̲̠H͚̝͡e̵͇̜̲̦͔ͅ ͎͚͇w͔̹̭̳h̟̙͝o̸̯̫̯ ̢̫̤͖̯͕W̤ͅͅḁ̟̻iț̛͍͍ͅs͇̮̗ ̹͕͙̭͎̰̺B͞e̥h̜i̲̹̠̳͡ͅn͚͓̝̹̞d̵̹̫̗̯̩ ͡T̗͕̹̣͚̘̗h͓e̡̮ ̖͉W͇͈̠̱͈͉̬a̯̱̩͉͔͟l̶̰̞̻͚̗l̰͈͕̲̭̙͈.̯͟
            ̮Z͏̠̩͚̥̺̻A̦͔̜͎ͅL̪͜G͉̳͍̀ͅO̭̠̞̲͈̟̭͡!̫̹̰̣
            ''', 
            'chaos') == []
        assert find_all_indexes('''
            Head underwater
            And they tell me
            To breathe easy for a while
            Breathing gets harder, even I know that
            Made room for me It's too soon to see
            If I'm happy in your hands
            I'm unusually hard to hold on to

            Blank stares at blank pages
            No easy way to say this
            You mean well, but you make this hard on me

            I'm not gonna write you a love song
            'Cause you asked for it
            'Cause you need one, you see

            I'm not gonna write you a love song
            'Cause you tell me it's
            Make or breaking this
            If you're on your way

            I'm not gonna write you to stay
            If all you have is leavin'
            I'ma need a better reason
            To write you a love song
            Today, today, yeah

            I learned the hard way
            That they all say
            Things you want to hear

            My heavy heart sinks deep down under
            You and your twisted words
            Your help just hurts
            You are not what I thought you were
            Hello to high and dry

            Convince me to please you
            Make me think that I need this too
            I'm trying to let you hear me as I am

            I'm not gonna write you a love song
            'Cause you asked for it
            'Cause you need one, you see

            I'm not gonna write you alove song
            'Cause you tell me it's
            Make or breaking this
            If you're on your way

            I'm not gonna write you to stay
            If all you have is leavin'
            I'ma need a better reason
            To write you a love song
            Today

            Promise me you'll leave the light on
            To help me see
            With daylight, my guide, gone
            'Cause I believe there's a way
            You can love me because I say
            I'm not gonna write you a love song
            'Cause you asked for it
            'Cause you need one,
            You see

            I'm not gonna write you a love song
            'Cause you tell me it's
            Make or breaking this
            Is that why you wanted a love song?
            'Cause you asked for it
            'Cause you need one, you see

            I'm not gonna write you a love song
            'Cause you tell me it's
            Make or breaking this
            Or you're on your way
            I'm not gonna write you to stay

            If your heart is nowhere in it
            I don't want it for a minute
            Babe, I'll walk the seven seas when I believe that
            There's a reason to write you a love song
            Today, today
            ''', 
            '\n') != []
        with self.assertRaises(AssertionError, msg='text is not a string: {}'.format(599)):
            find_all_indexes(599, '420')
        with self.assertRaises(AssertionError, msg='pattern is not a string: {}'.format(420)):
            find_all_indexes('599', 420)


if __name__ == '__main__':
    unittest.main()

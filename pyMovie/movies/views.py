from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
import random


from django.template import loader

from .models import Movie, MovieForm

rom = ['You are my light as well as my burning desire.',
 'Loving you is not a beginning or ending; it is the path of growing together.',
 "I don't have eternity on earth, but I hope to do everything on earth with you.",
 'I know what love is, thanks to you.',
 'My heart wants to sing in the hopes to speak your love language.',
 'I want to build bridges with you, never walls.',
 "Being with you teaches me what I've never been; but always wanted to be.",
 "It isn't gazing into your eyes, but rather us looking at a shared future that excites me.",
 'Your love lifts me out of the muck I can get stuck in during daily life.',
 'Kind words can create confidence. Kind thinking can be profound. But your kind giving of time creates love.',
 'When you are in my life, there is love. ',
 'You make my life home.',
 'Just in case you need it: You are wonderful, loved, and amazing!',
 "Getting older doesn't protect you from loving, but building love can protect you from feeling older. ",
 'Love is one of the few true adventures. I enjoy our adventures together.',
 'I have no remedy for loving you, just the addiction that I need more.',
 'The supreme happiness in my life is in the conviction of knowing how much I love you.',
 "I know you aren't a perfect person, but I your imperfections make you unique and wonderful.",
 'Love is at the soul of genius; if something I said sounds smart, you are my muse.',
 "I'll never feel broke, because I am rich in your love.",
 'Being silly with you appears simple, but feels so amazing.',
 'A life dipped in our love will never lose its shine.',
 'I may not have much, but I will do my best to be generous with my attention and time.',
 'Loving you makes the walk through life a pleasant stroll.',
 'Love is a regular lesson, there is no end result. I am glad to be sharing this education with you.',
 'You are more than enough for me. Thank you for existing!',
 'I am amazed at the time we get to spend together; it never feels like enough.',
 'Our weekends together are amazing; the only thing better was having even more time with you!',
 'The power of you and I can go anywhere we desire; because our love knows no bounds.',
 "There is always something new to love about you; that's one reason you are a wonderful teacher.",
 'I enjoy our moments together; because those daily moments reflect love like light on a lake.',
 'No mortgage is due when you live in my heart.',
 "I never worry if I am crazy or absent-minded, so long as we are together I know I'll be fine.",
 "Your love is like a magic trick that I can't quite figure out, but want to keep watching to be amazed.",
 'Our love is like a song that only we can hear.',
 'The madness of loving you is what makes it feel so flawless.',
 'Yesterday, tomorrow, a month, a year, a decade, and more: I love you',
 'Loving you is like knowing the future; I know my life will be amazing so long as you are in it.',
 'Thinking of you opens my eyes, dreaming of you closes them, and being with you gives me insight into life.',
 'I can not measure how much love my heart can hold for you.',
 'Love is being silly together',
 'I need no reason to love you; I simply do.',
 'The pull of our love brings waves of happiness in my life.',
 'My heart takes flight when I wake and celebrates another day with you.',
 'I love you in the moment-to-moment breath of life, simple and awe inspiring.',
 'Loving you is like creating art, it brings harmony out of the chaos of daily life.',
 'Love can turn us upside down, twirl us around, and make us wanting to ride it more.',
 'The greatest three words are not I love you, but rather: How are you? I want to learn more, because I love you.',
 'If romance is the icing, our love is the cake.',
 'I may not always understand, but I will love you and cherish you.',
 'You make my life better with every breath you take.',
 'I wish I could use my kiss to tell you all the words in my heart.',
 'You are a beautiful woman that I am glad to have in my life.',
 'The best path to walk down is the one where we can go hand in hand.',
 'If I distilled all my ambition, I am sure it would come down to loving you and being happy in all the adventure we find.',
 'Love is divine, which is why your kiss is angelic.',
 "I don't think I will ever be able to give you enough love, but I find joy in my daily attempts.",
 "Love makes us shine in ways the sun couldn't comprehend.",
 'You rekindle the silliness in me.',
 'Small acts of kindness and love may be forgotten, but they make the mood and tempo of our lives together a joyful song.',
 'Your happiness is essential to my own.',
 'You are my best friend and my wonderful partner in this life.',
 'If I am judged by the company I keep, I am fine with that, because you are by my side.',
 "I love you not because you don't fall, but because of how you pick yourself back up.",
 'Inside myself is a place I build because I want to share it with you.',
 'Loving you makes me understand how joyful this world truly is.',
 'I admire the beauty of the life we are creating.',
 "I don't want to waste a minute with you, because our life together is precious to me.",
 'Love and time must not mix, because without you feels so long; but being together with you feels so short.',
 'I know our love will travel as far as we let it, but can always be found in the space our hugging.',
 'Our home is a warm nest because of all the beautiful memories we share.',
 "The love we've built serves, thinks careful, and is humble. Thank you!",
 'Your friend, your love, your husband; no matter the title, I am glad to be here with you.',
 'Our love is like a feast, it takes time to tend and build, but is a joy / delight to share every day.',
 'The joy we share requires both of us, for it would only be half as sweet with just the one.',
 'What an amazing world do I live in, when the person I admire the most puts their head next to mine every night.',
 'The love we build is what makes our memories together so sweet.',
 'To hear you and acknowledge your day is one of the best ways to say I love you, without a single word.',
 "I sometimes watch you with love, hoping that my eyes will say the words my mouth isn't capable of saying.",
 'If music is the voice of love, than I can think of no better song than saying your name.',
 'Our hearts are like magicians, making romance and amazing things bloom from thin air.',
 'I love the way I am becoming, because you are in my life.',
 'If I wished upon a shooting star, I would wish it to happen twice; just so we could share the experience together.',
 'I want to be the connoisseur of your wonderful company and our shared joy together.',
 'In a world of sparkle and bling, your love is what made me put on this gold ring.',
 'I love your faults, not because they are small, but because they are part of who you are.',
 'I am grateful to be able to afford the luxury of your time and love. The only thing I can repay it with is my own time and love.',
 'My dreams include your happiness because I love you and want to see your heart shine.',
 'The beauty of your soul is an amazing treasure I enjoy admiring daily.',
 'Our love is a game we both play and both win.',
 'We share not just a union of bodies, but a union of our souls. That is why your happiness is my happiness.',
 'Your love is my reward.',
 'Our love is like a friendship set to an unhearable music or rhythm.',
 "The ultimate expression of the will to live is our love and the life we've built together.",
 'I enjoy the love we share and the moments that connect the mundane to the extraordinary.',
 "Our love is less a noun, and more a verb. It's not a thing we have, but a doing word.",
 'Our love knows no bounds. It would jump fences, break through walls, and swim moats; just to say hello.',
 'I am happy because I love and am loved by you.',
 'Our love is like a fruit that is in season year round.',
 'The more I learn about you, the more I come to love who you are.',
 'Your happiness brings me peace throughout my day.',
 'At the foundation of my existence is a growing love and respect for you.',
 'Our life together provides the freedom to grow and intertwine our days together.',
 'Your love lights the darkness of the night and helps point the path towards the future.',
 'There is little surprise in my heart that I love you so much; it was something that happened naturally and continues to grow.',
 'No matter how dark night gets your heart shines in my life',
 'Living together with you makes my life beautiful',
 'I know that the strength of our family will grow in the rich soil of our love and understanding',
 'While you teach kids at school, you teach me more things to love about you at home',
 'My heart tells me to hold your hand and never let go',
 'Feeling you in my arms is like holding sunshine',
 "You lift me higher every day and yet, I can't help but look up to how wonderful you are",
 'If we live moment to moment, I am excited to see where our moments take us next.',
 "I love living in the music we've built surrounding us",
 'My love for you is a boomerang, the more I send out, the more I feel coming back in.',
 'It is easy to say I love you; harder to show you in deeds. I hope the words you hear the best have no sound.',
 "I don't need everyone to love me; just you",
 'I am a huge fan of your smile, care, and touch.',
 "I can't say who I'll become, but I hope to shape that future with you.",
 'Spending the night watching fireworks reminds me of the spark of love you ignite inside me daily.',
 "You appear in my dreams at night, so that I don't have to worry about closing my eyes.",
 'I fall in love with you every time we are together.',
 'There are many styles of love out there, but our style is my favorite.',
 'When you wake up, when you get ready, when you go through your day, when you come home - my heart follows you.',
 "I don't know if magic exists, but I do know our love feels magical.",
 'On the couch, you sometimes fall asleep in my arms and I can think of no better feeling than your warmth and contentment.',
 'I hope to provide no chase for my love, for I give it freely and whenever you want.',
 'The more I pour into our shared love, the more I get out.',
 'Our love brings security and happiness to our home',
 "Choosing to be in love is not the same as falling in love. We don't share an accidental love, but rather a deep well of shared creation.",
 "I hope to always be available for your love, because it is precious to me and I don't want to miss the opportunity.",
 'I would go much further for you, but will always prefer you as close as possible.',
 'If life is a box of cracker jacks; full of nuts and sweets, you are the prize that I always dig for.',
 'You are the stars and moon in my night sky, the sunshine in my day',
 'Your touch, subtle and soft, feels major and important to me',
 'If I built a day, I would start with us cuddling in bed. From there, I would call it good.',
 'Seeing the impact you make on those around you always builds wonder and amazement in my eyes',
 'You live in my heart and I hope that my eyes always reflect that truth',
 'Our love story is the best! It is one that involves bears, cuddling, and us.',
 'I look forward to our love building and evolving throughout the years',
 'You are amazing to me, like a painting come to life',
 'Your kiss feels like a warm summer breeze, but can still send shivers down my spine',
 'You bring happiness and joy to my life. I can not tell you how amazing you truly are to me.',
 'My joy often revolves around how I can provide warmth to your life',
 'Our life is both a deep calm passion and a wonderful improptu dance; thank you for an amazing life together!',
 'I know we may make mistakes, but I enjoy us working on correcting them together',
 'You let me be myself in a way I am sometimes afraid to express, that is just one reason I love you',
 'If I can help build love in your heart, I know everything will turn out okay',
 'Our love will find a way, even if through paths were wolves fear to prey.',
 'I am grateful that you have shown me your love, and I am excited to continue to show you mine',
 'I love who we are together',
 'Our love is like a song based in friendship, silliness, and trust',
 'The love we share is like a spiritual fire, calming and warm',
 "Our love doesn't know any walls. It busts through past conventions and shows up like the Kool-aid man.",
 'I am happy to know your love, it feels me with honor and thanks.',
 'The love we share is the strongest passion, for it savages my mind, heart, and senses; leaving me stunned.',
 'If flowers grew whenever I thought of us, the garden would go on forever.',
 'When I awake in the morning, I am grateful to have you next to my side.',
 'It is impossible for me to ever get enough of your love, just as I know I will never be able to give you enough of my love.',
 'If I were a tree, you would be the fruit. For everyone recognizes the type of tree by the fruit.',
 'I want your love, so it is with great hope that I am lovable to you. But if not, I hope that you at least feel how lovable you are to me.',
 'Love is not a dominating force, it is a cultivating one. I look forward to growing old with you.',
 'Sometimes love is an untamed force. If we try to control it, it can destroy. But if we dance with it, it will dance back.',
 'I am most alive when I have you in my arms.',
 'Our love is an education in itself and I a hungry student.',
 'Hate is too much of a burden to bear, so I would rather love you and a bear.',
 'You add quality and beauty to my life',
 'Being with you feels like spoiling myself',
 'Let our mouths stop superfluous words by sealing them with a kiss',
 'As you return to school, I know just how lucky those students are; because they get to spend time with you.',
 'You give me strength and courage throughout my day',
 'You reveal new truths about myself through our love',
 'The way we love may not be pronounced with large bells, but it still rings true through the core of me',
 'Our love is not simple something felt, but it is something that drives me to action',
 'I am grateful to have your love, for being loved is everything',
 'We build our own world together, where we share our joys and loves daily; it is an amazing place.',
 'Where I am alive, I am in love with you',
 'Both fortune and love favor the brave, which is why I enjoy our adventures together',
 'As our love grows, it gives me confidence in my highest hopes and wildest dreams',
 'I am never alone, for you are always in my heart',
 'You steal my breath with your kiss and I am grateful for the act',
 "I don't know if there is a time and place for love, it just happens in odd places, like bowling alleys",
 'Our home is not built with wood or stone, but in our hearts together.',
 'I sometimes wonder if the universe works for us, because it feels like the planets revolve around you',
 'Times may sometimes be hard, and it may require work, but I want to do that, because it would mean I am with you.',
 'Your heart frees me from the weight of the world and lifts me up',
 'The feeling we have is sometimes like wind; you may not be able to see it, but you can feel it rushing all around you.',
 'I know that love may make us vulnerable, but I would gladly take that risk with you any day.',
 'My heart sang half a song, until you came in with the chorus.',
 "I don't love you for your looks, clothes, or fancy necklaces; I love you because of what I see inside of you.",
 'Your love drives away the darkness of fear, like a bright light shining against the backdrop of night.',
 'Love isolates us by driving us to build a world with just us.',
 'I do not want to repress my feelings, instead I want them to flow freely so I can tell you how much I admire and love you.',
 'When I say your name, I hope you hear it said in a different tone. For every time I speak it, I add some love intertwined.',
 'I can give you no better gift, than the gift of my time and attention.',
 'Our love can not be pulled from me, and I will always feel it for you.',
 'Love at first sight is misleading. I love you every time I see you.',
 'I would risk much, just to keep and hold you. For you are a treasure in a world of mundane.',
 'Our love is a promise because it is a decision and judgement that we keep together throughout our days.',
 'I hope you know how wonderful and amazing you have made my life so far.',
 "I don't expect anything from our love, instead I only want to give anything I can to it. As it grows, I grow.",
 'I will love you when my hair changes color and my bones weaken. I will love you when I am young and stong. I love you now, then, always.',
 'You pull down the sky and put stars in my eyes, which is why I am amazed at the sight of you.',
 'I can think of no better heater than the warmth of your body next to mine.',
 'My love for you reaches further into me, because it searches for ways to grow us together.',
 "As the ages change, and new things capture our gaze, I look forward to turning to the side and showing you what we've found together.",
 'I love watching the lines of your lips, like a roller coaster; the windup of leaning in, the excitement of your touch.',
 'Together we build a house into a home, but in our hearts we build our lives into love.',
 'I enjoy football, not so much for the sport, but for holding you close against me and feeling your warmth.',
 'With the touch of love, everyone becomes a poet, which is why I feel the need, to let you know it.',
 "Our love is not a wildfire, burning lives away. Instead it's a fireplace on a winter night, keeping us cozy and cuddled up together.",
 'Like night vision goggles, you light up the night; like heat sensing infrared, you turn hot in my sight.',
 'Together we share quiet words that echo throughout my days.',
 "In the morning, we wake up together, in the night we go to bed together. That's how I know life is on track.",
 'I enjoy your kisses, like dew drops off a spring flower, sprinkling across my tongue',
 "While we can't plan for love, if I were to make a plan, your love would exceed all my wildest ambitions.",
 'When I am near you, I lose focus on how big the world is, because I realize that you are my world.',
 "You never talk down about me being silly, instead, you are silly with me. That shows you understand the truth: life's too short, not to laugh together.",
 'Your eyes make me wonder what worlds they see, but what I wonder most, is how I can make the world as beautiful for you as you are to me.',
 'When our fingers intertwine, tit feels  like knots, because to unclasp your fingers feels so difficult.',
 'I may say I love you a lot, but there is a reason for that: I mean it! Today, tomorrow, and always.',
 'If I hold you, I feel you close. If I kiss you, I feel you close. If I whisper in your ear, I feel you close. But no matter all these things, I never feel close enough.',
 "Our love can build a wild and amazing future, but to us, most days may seem mundane. That's why I enjoy taking a moment to",
 'Having you near makes the world feel far away.',
 'Thank you for the amazing wonders you bring into my life everyday.',
 'The morning brings me wonder; for I can look to my side and see you in my bed and I wonder: how am I so lucky?',
 'Each breath you breath is a tiny gift to me, for your very existence is wonderful.',
 'If I had a cloning machine, I would never attempt it on you. It would be too great a risk that the universe would say you are too unique and wonderful to emulate.',
 'Every day brings a little kindness to my life, for I get to share that day with you, and how wonderful that feels to me.',
 "It's hard to let go when we weave our hands together.  Instead I choose to pull you closer.",
 'As the leaves change color, know that my heart beats a deeper shade of love for you every day.',
 'If I had a way to spend the day in your embrace, I would know that it was a day well spent.',
 'The way you show your love humbles me and makes me wonder how amazingly lucky I am.',
 'Our love is not a day time thing, but an all the time thing. In my dreams, during my workday, the evening, and beyond.',
 'I enjoy everyday a little more, because I know you are in it.',
 'Thank you for the light and warmth you bring into my life.',
 'My wonderus love, you sparkle my eyes and take my breath away; thank you for being a feast for the senses.',
 'I love the very fabric of who you are.',
 'If I had a method to describe the depth of feeling I have for you, it would be a best selling book.',
 'I may not know what the future holds, but so long as I hold you, I will be glad to meet that future.',
 'I long for your touch and desire to hear your whispers, even if the action is shaking me away to ask where PJ is.',
 'If I had to design a perfect woman, I would give up immediately, because I could never have imagined someone as wonderful as you.',
 "I enjoy our evenings, mornings, and weekends together. It's these moments where I feel the most alive.",
 "I see the amazing things you do everyday and get to sit back + admire you. It's a wonderful position to be in.",
 'Our love reflects like a wonderful reflection off a pond; tranquil, full of light, but with an untold depth.',
 'Today is the best day, because it is the only one with you in it. The past holds what I remember of you, the future what may be, but you are here with me now.',
 'I know whatever we may face, it will be smaller, because we will face it together.',
 "If our love was a math equation, it wouldn't be addition or multiplication, it would be the golden ratio because it turns the daily to beauty.",
 'My heart sings a song only your heart can hear.',
 'I enjoy the seconds, minutes, hours, days, months, years, and decades we get together. All are precious moments to me.',
 "I don't have to ever wonder what it would be like growing up together, because I would rather choose growing old together.",
 'Your excitement, your wonder, your love is what fuels me every day.',
 'I want very little from this world, because it has already given me you.',
 'I wonder what magic floats between our love, how can it transform everyday into something more?',
 'I am not sure I believe in magic but I believe in our love.',
 "I've found true love never happens suddenly, instead it takes time and is a hard process. I am glad to forge these bonds with you.",
 'I am thankful to have you in my life. Thank you, thank you, thank you!',
 "True love is a solid rock, to which I am glad to cling to what we've made together.",
 "Our love isn't a finite supply, instead the more we pour in, the more we get out.",
 'I hope you know how much I love you with each gentle cheek caress and kiss on the forehead.',
 'If two becomes one, I can understand why they say you are my better half.',
 'I know you are not perfect, but I admire the ways you are handle yourself daily.',
 "I don't need to bet on you making me happy, I know you will everyday.",
 'If I had a wonderful machine that could make dreams come true, it would sit idle, because I am already here with you.',
 "Sunshine doesn't seem that warm when compared to holding you in the night.",
 "If there are two things in this world I enjoy the most, it's hearing about your day and watching you sleep nestled in my arms.",
 "I am not sure where I'll go in this life, but I know I'll enjoy the journey with you along the way.",
 'Many things can build a house, but our love is the only thing that will make it a home.',
 'I wonder if I should gamble more often, because being with you makes me wonder how lucky I truly am.',
 'Our love blossoms everyday with a single "Good morning".',
 "I don't need to hope to find treasure in my old age, when the true treasure is getting to share our lives together till old age.",
 'Many things can be said about love and romance, but most things can only be felt.',
 'I know that time can move quick, but know that our time together helps set the pace for everything else.',
 'I wonder if the stars look down on us and wonder, how did the miracle of our love happen in the cosmos?',
 'Many pieces can make a whole, but as two whole beings, I never feel complete until we are together.',
 'Our love is self replicating; the more it shows up, the more it produces another round of love.',
 'If I had the perfect song, I would sing it to you. But I don\'t have that talent, so I am left with a simple "I love you".',
 "The levers of life cause us to be moved in many directions, but as long as it's home with you, I am fine with that.",
 "I don't know if I make mistakes all the time, but I hope to learn and grow our love through them, like flowers springing from gravel.",
 "Today may just be 24 hours, but if it's spent with you, I can tell it will be 24 well spent hours.",
 'The clock circles us and warns us of impending deadlines. Our love holds the clock hands still and tells us the truth of what is really important.',
 'Your winter break starts so late, but I am so grateful to spend the time with you.',
 'I am excited to spend Christmas unwrapping new adventures together with you.',
 'Our love is the best on every calendar event that ends in "day". (Monday, Weekday, Saturday, etc.)',
 'Today is an amazing day, because you are in it.',
 'Our love shows me a passage to a wonderful today, tomorrow, and future.',
 "As the new year starts, I am grateful for all the years we've shared so far, and excited for the one to come.",
 'Our love reminds me of flowers in a meadow, peaceful, full of color, and somehow exhilarating',
 "I don't know if I can produce miracles regularly, but I know that having you in my arms was nothing less than miraculous.",
 'This life is both long and short. It takes so long to get home to your embrace, which moves so fast into the next day.',
 'Together we embrace the day with our love and understanding. With luck, the day embraces us back with growing that love and understanding.',
 "I see many ways that you are wonderful; though I am not sure I can can't them all out, as that would take too long.",
 'This day is a blessing because you are in my life.',
 'Thank you for all the love and trust you make a daily occurrence in my world.',
 'There are many wonderful places to go in this world, but I can think of none more amazing than by your side.',
 'If our love was a deep reflective pool, I would train to be the worlds best swimmer. For I would long to hold my breath and embrace you fully.',
 'I may not be able to count on everything going to plan, but I can plan on figuring it out together with you.',
 'The hope and love we share makes everything around us blossom with extra color and vitality.',
 'This day is an amazing wonder, because I get to share it with you.',
 'I hope that you know the thankfulness and gratitude I have for the universe; for it brought you into my life.',
 'Our love amazes me and puts a glean of wonder in my eyes.',
 'I know that I will never be alone, for even when I am alone, you are here in my heart.',
 'You are in my dreams and my heart.',
 'Today is a blessing, yesterday was a blessing, tomorrow is a blessing. What do these days have in common? I get to spend them with you.',
 'I look forward to growing together in love and trust.',
 'Many things can lead us to decisions, but I know the best decision is spending the day with you in my arms.',
 'I hope you know that you are a blessing in my life',
 'I am grateful for the love we share and build daily',
 'Our love has this amazing power to grow with nothing more than holding each other close',
 "Today may seem quick and fleeting, but if it's spent with you, I know it will be well worth it",
 'I hope nothing more from tomorrow than sharing it embraced with you',
 'If our love continues to grow, I wonder how much it will change our futures. It is a mighty wonder I look forward to discovering.',
 'Your eyes reflect my face, looking at you in love and reverence',
 "May the day include time together, and the night include time spent in each other's dreams.",
 "I love you in ways I can't fully say, but I look forward to finding a way.",
 'Thank you for being in my life, and for letting me be in yours.',
 'Every day, all day, I am glad and grateful for the grace and love you show me.',
 'Yesterday may be in the past, but I know I can look at it warmly because we shared it together.',
 'I can use many descriptions to show our love, but the best way to describe it is with time and a soft embrace.',
 'Thank you for the wonder you give to me on a daily basis.',
 'Our love grows each day, and for that, I am grateful for whatever it is growing towards.',
 'Sunshine may bring light to the darkness, but your warmth brings the sunshine to my heart.',
 'I enjoy the little things we share, and hope that we can revel in those little things for many long days.',
 'I love you throughout the day, week, month, year, and decades.',
 'There is little surprise in my heart that I love you so much; it was something that happened naturally and continues to grow.']

def index(request):
    latest_movie_list = Movie.objects.filter(type="Movie")
    shows = Movie.objects.filter(type="Show")
    context = {
        'rom' : random.choice(rom),
        'latest_movie_list': latest_movie_list,
        'shows': shows
    }
    return render(request, 'movies/index.html', context)



def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'rom' : random.choice(rom),'movie': movie})

def mov_rando(request):
    latest_movie_list = Movie.objects.filter(watched=False, type='Movie')
    movie = random.choice(latest_movie_list)
    print(latest_movie_list)
    print(movie)
    return render(request,'movies/mov-rando.html',{'rom' : random.choice(rom),'movie': movie})

def show_rando(request):
    latest_movie_list = Movie.objects.filter(watched=False, type='Show')
    movie = random.choice(latest_movie_list)
    print(len(latest_movie_list))
    print(movie)
    return render(request,'movies/mov-rando.html',{'rom' : random.choice(rom),'movie': movie})

def add(request):
	print("add call")
	if request.method == "POST":
		movie_form = MovieForm(request.POST)
		if movie_form.is_valid():
			movie_form.save()
			messages.success(request, ('Your movie was successfully added!'))
		else:
			messages.error(request, 'Error saving form')
		
		
		return redirect("movies:index")
	movie_form = MovieForm()
	movies = Movie.objects.all()
	return render(request=request, template_name="movies/add.html", context={'rom' : random.choice(rom),'movie_form':movie_form, 'movies':movies})

def watched(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	movie.watched=True
	movie.save()
	return render(request, 'movies/detail.html', {'rom' : random.choice(rom),'movie': movie})

def search(request):
    if request.method == "POST":
        keyword = request.POST['search']
        print(keyword)
        latest_movie_list = Movie.objects.filter(type="Movie",title__icontains=keyword)
        shows = Movie.objects.filter(type="Show",title__icontains=keyword)
        context = {
            'rom' : random.choice(rom),
            'latest_movie_list': latest_movie_list,
            'shows': shows
        }
        return render(request, 'movies/search.html', context)
    
def watching(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	if movie.currently_watching:
		movie.currently_watching = False
	else:
	    movie.currently_watching = True

	movie.save()
	return render(request, 'movies/detail.html', {'rom' : random.choice(rom),'movie': movie})

def we_watching(request):
    latest_movie_list = Movie.objects.filter(type="Movie", currently_watching=True)
    shows = Movie.objects.filter(type="Show",currently_watching=True)
    context = {
        'rom' : random.choice(rom),
        'latest_movie_list': latest_movie_list,
        'shows': shows
    }
    return render(request, 'movies/index.html', context)

def xmas(request):
    latest_movie_list = Movie.objects.filter(xmas=True)
    context = {
        'rom' : random.choice(rom),
        'latest_movie_list': latest_movie_list,
    }
    return render(request, 'movies/index.html', context)
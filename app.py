from flask import Flask , render_template , url_for

app = Flask(__name__)

blogs = [{'title': 'You re the shooting star of my night sky ','date': '23-02-23','image':'/static/images/CardImg1.png'},
{'title': 'You, me, and our cup of coffee','date': '24-02-23','image':'/static/images/CardImg2.png'},
{'title': 'The hat of love','date': '25-02-23','image':'/static/images/CardImg3.png'},
{'title': 'Chemistry behind first love','date': '23-02-23','image':'/static/images/CardImg4.png'},
{'title': 'Till the last breath','date': '23-02-23','image':'/static/images/CardImg5.png'},
{'title': 'The love potion','date': '23-02-23','image':'/static/images/CardImg6.png'},
{'title': 'Can love exist without friendship?','date': '23-02-23','image':'/static/images/CardImg7.png'},
{'title': 'Love knows no genders','date': '23-02-23','image':'/static/images/CardImg8.png'},
{'title': 'Eyes chico, they never lie','date': '23-02-23','image':'/static/images/CardImg9.png'},
{'title': 'hello friends this is awosome h w w wwe rwrwrwee etert eter tet erdfsdfe45e4te4t terter ','date': '23-02-23','image':'/static/images/CardImg1.png'}]

big_blog =[{'b_title':'You re the shooting star of my night sky','b_subtitle':'Can love exist without friendship?','b_date':'01-03-2023','b_image':'/static/images/Mainpic.png'}]

detail_blog =[{'date':'27-02-23',
'title':'Can love exist without friendship? welcome back',
'subtitle':'ye hai subtitle of this blog',
'writer':'Aniket Kumar ',
'image':'/static/images/MainPic.png','image2':'/static/images/MainPic2.png','image3':'/static/images/MainPic3.png',
'content':'It was just a hat. A bowler or derby hat. I saw it hanging on a hat stand in Magikat Books and Magic Emporium. I passed by it daily on my way to work. The shop itself was hardly what might be imagined as an emporium. It seemed small and unobtrusive, but the hat fascinated me. But the hat fascinated me so much that I ventured inside. The shelves of books had no interest, but the hat held my attention. I saw myself wearing it but thought it would bring a smile or even a few derisive comments from my workmates. I tried to put it out of my mind and left the shop and went to work. But there it was still, every day. I made up my mind to have it if it was for sale.',
'content2':' The next morning when I passed the shop on my way to work, there it was, back on that stand, almost brazenly daring me to go in! The door rang a bell as I entered. A little, wizened fellow stood behind a counter with a knowing smile on his face. He wore a patched grey jacket and a once-white shirt and a blue bow tie. His hands were clasped in front of his chest. <br>',
'content3':'  His knowing smile broke into sound, “You’ve come for the hat, haven’t you!” It wasn’t a question.I nodded, “How did you know?”<br>“You pass by every morning and look at it. The hat told me you would like it.” <br>“But it wasn’t there yesterday. I thought someone else had bought it.”<br>“A man did, but it came back the same day.”“Oh,” I said. “May I try it on?”“No need. It will fit you perfectly.”<br>I took the hat down from the stand and placed it carefully on my head. I’m sure I felt it settle and it fitted perfectly. “How much,” I asked.“Oh, you can have it for as long as you need it.”I was overwhelmed and thanked him profusely. <br>“See you again, eh?” The knowing smile reappeared. I tipped my new hat at him and left the shop feeling I had scored a bargain!<br>I wore it into my office and was surprised there was little or no reaction. I went to take it off, but it was stuck. It simply wouldn’t budge. I had quite a lot of work to do, so I left it on and started going through my clients’ accounts. It was tax time and an accountant’s life was a busy one. Today the work seemed easy, and I flew through at least twice as many accounts as normal. The hat stayed on. I was happy wearing it. I ate my lunch at my desk and continued working through the afternoon. By five o’clock I had finished what was a week’s work.',
'content4':'I couldn’t really understand why. I walked home, with what I’m sure was a jaunty gait. Once at home and the front door, I went to take my hat off and it came off easily. I placed it carefully on the hat hook on the wall. My phone rang and it was a young lady from my office I had fancied for some time but was too shy to ask her out. She asked me out! She said she was very taken with her hat and couldn’t resist getting to know me outside of work. Of course, I agreed, and we had a wonderful evening that turned out quite romantic. She was perfect for me, and we seemed to get on so well together. She asked if could we see each other again. You bet I said. I went home elated.As I opened the front door, I noticed my hat was missing from its place on the wall. I thought I’d been broken into, but nothing else was missing. But I was in such a state of joy, I decided not to worry about it and enjoy a happy sleep, dreaming of my new friend. The next morning, I skipped out of the door, stopped, and went back inside. There on the wall was my hat. I looked at it and thought I had somehow just missed it the night before. I gleefully put it on and went happily to work. As I passed the bookshop I tipped the brim to the hat stand, thinking that the old fellow was probably standing behind the counter with that smile on his face, watching me walk past. He would surely notice the spring in my step. <br>I arrived at the office and my new friend smiled at me and said quietly that the boss, the senior partner, wanted to see me. She squeezed my hand discretely and I smiled at her. The senior manager told me that his phone hadn’t stopped ringing with calls from my clients expressing their joy at what I had been able to do for them. I was pleased. Then he said that I was to be his new partner! What a day! <br>I whizzed through the day and on my way out I asked my new friend to celebrate with me. She smiled and said she couldn’t think of a better idea. At home, I took off my hat and kissed it before putting it on its hook. Again, the evening was superb, and I realized I was hooked on my lovely friend. The next morning, I was about to leave and noticed my hat was missing, I searched for it, but it was nowhere to be found. I was mystified and quite upset. But I had to be at work on time, on my first day as a partner. As I passed the shop, I couldn’t help but look in. There was my hat on the old hat stand! But how? I went in and asked the old gentleman how my hat was back. <br>He smiled that knowing sort of smile, “You don’t need it anymore.” I looked at the hat and I swear it tilted its brim at me '},{'type': 'text'},{'type': 'image'}]

detail_Card_blogs=[{'title': 'You re the shooting star of my night sky ','date': '23-02-2023','image':'/static/images/CardImg1.png'},
{'title': 'You, me, and our cup of coffee','date': '24-02-2023','image':'/static/images/CardImg2.png'},
{'title': 'The hat of love','date': '25-02-2023','image':'/static/images/CardImg3.png'}]



@app.route('/')
def home():
    return render_template('index.html', posts=blogs,bBlog=big_blog)

@app.route('/blog')
def blog():
    return render_template('blog.html', detail_blog=detail_blog,detail_Card_blogs=detail_Card_blogs)  
if __name__=="__main__":
    app.run(debug=True , port=900)
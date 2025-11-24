from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse


app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World!"}

text_posts = {
  1: {"title": "Exploring the Wilderness", "content": "Had an amazing time hiking in the mountains this weekend! The views were incredible. Check out this photo of the sunrise! #WildernessAdventure #NatureLover"},
  2: {"title": "Cooking My Favorite Dish", "content": "Tried cooking lasagna from scratch today! It turned out delicious, but a bit messy. Here's the video of me layering it up. #Foodie #HomeCooking"},
  3: {"title": "Sunset at the Beach", "content": "Nothing beats a sunset by the beach. So peaceful and calming. Take a look at the video of the waves crashing at sunset! #BeachVibes #SunsetLover"},
  4: {"title": "My New Artwork", "content": "Just finished a new painting of a cityscape. It’s my biggest piece yet! Here's a pic of it before I framed it. #Art #CreativeProcess"},
  5: {"title": "Yoga in the Park", "content": "Had a peaceful yoga session this morning in the park. The weather was perfect! Here’s a quick video of me doing some sun salutations. #YogaLife #MorningVibes"},
  6: {"title": "Road Trip Adventures", "content": "Started a cross-country road trip today! First stop: a quirky little diner in the middle of nowhere. Here's a picture of the place! #RoadTrip #TravelGoals"},
  7: {"title": "Rock Climbing Challenge", "content": "Just completed my first rock climbing course! It was tough but so rewarding. Here’s a video of me making it to the top! #ClimbingLife #ChallengeAccepted"},
  8: {"title": "Concert Night", "content": "Went to a live concert last night. The band was amazing! Check out this short clip of their performance. #LiveMusic #ConcertVibes"},
  9: {"title": "New Book Recommendation", "content": "Just finished reading this incredible book about space exploration. Highly recommend it to anyone interested in the stars. Here’s a photo of the cover. #Bookworm #SpaceScience"},
  10: {"title": "Baking a Cake", "content": "Baked my first ever chocolate cake today! It’s not perfect, but it tastes amazing. Here’s a quick video of me frosting it! #Baking #SweetTreats" }
}

@app.get("/posts")
def get_all_posts(limit: int = None):
  if limit:
    return list(text_posts.values())[:limit]
  return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
  if id not in text_posts:
    raise HTTPException(status_code=404, detail="Post not found")
  return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
  new_post = {"title": post.title, "content": post.content}
  text_posts[max(text_posts.keys()) + 1] = new_post

  return new_post
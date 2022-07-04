import hashlib
from aiogram import types, Dispatcher
from youtube_search import YoutubeSearch as YT


def finder(text):
    result = YT(text, max_results=10).to_dict()
    return result


async def inline_youtube_handler(query: types.InlineQuery):
    text = query.query or "echo"
    links = finder(text)
    articles = [
        types.InlineQueryResultArticle(
            id=hashlib.md5(f"{link['id']}".encode()).hexdigest(),
            title=f"{link['title']}",
            url=f"https://www.youtube.com/watch?v={link['id']}",
            thumb_url=f"{link['thumbnails'][0]}",
            input_message_content=types.InputMessageContent(
                message_text=f"https://www.youtube.com/watch?v={link['id']}"
            )
        ) for link in links
    ]

    await query.answer(articles, cache_time=60, is_personal=True)


def register_inline_handler(dp: Dispatcher):
    dp.register_inline_handler(inline_youtube_handler)

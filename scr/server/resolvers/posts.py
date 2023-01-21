from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import Post


def get(post_id: int) -> Post | None | dict:
    res = dbmanager.execute_query(
        query='SELECT id, name_post, master_id FROM post WHERE id=(?)',
        args=(post_id,))

    return None if not res else Post(
        id=res[0],
        name_post=res[1],
        master_id=res[2]
    )


def get_all() -> list[Post] | dict:
    posts_list = dbmanager.execute_query(
        query="SELECT id, name_post, master_id FROM post",
        fetchone=False)

    res = []

    if posts_list:
        for post in posts_list:
            res.append(Post(
                id=post[0],
                name_post=post[1],
                master_id=post[2]
            ))

    return res


def delete(post_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM post WHERE id=(?) RETURNING id',
        args=(post_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_post: Post) -> Post | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO post (name_post, master_id) VALUES (?, ?) RETURNING id",
        args=(new_post.name_post, new_post.master_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(post_id: int, new_data: Post) -> Post | dict:
    res = dbmanager.execute_query(
        query="UPDATE post SET (name_post, master_id) = (?, ?) WHERE id=(?)",
        args=(new_data.name_post, new_data.master_id, post_id))

    if type(res) != dict:
        res = get(post_id)

    return res

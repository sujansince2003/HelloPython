from db import db, conn
import bcrypt


def create_user(validated_data):
    try:
        data = validated_data.model_dump()
        hashed_pw = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
        hashed_pw = hashed_pw.decode("utf-8")
        """
        data["password"].encode("utf-8") -> Convert string password → bytes
        bcrypt.gensalt() -> generate random salt
        bcrypt.hashpw(password_bytes, salt) -> Hash password using bcrypt + salt
        hashed_pw.decode("utf-8")-> Convert hashed bytes → string for DB storage
        bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8")) -> for checking pw during login 
        """

        db.execute(
            "INSERT INTO users (username,email,password,age) VALUES (%s, %s, %s, %s) RETURNING id",
            (
                data["username"],
                data["email"],
                hashed_pw,
                data["age"],
            ),
        )
        user_id = db.fetchone()[0]
        conn.commit()
        print("saved to db")
        return {"status": "success", "user_id": user_id}
    except Exception as e:
        conn.rollback()
        print("error saving to db:", e)
        raise Exception("failed to save to db")

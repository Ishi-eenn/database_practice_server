DROP TABLE IF EXISTS 本棚;
CREATE TABLE 本棚 (
  ID INTEGER PRIMARY KEY,
  タイトル TEXT NOT NULL,
  内容 TEXT NOT NULL,
  リンク TEXT,
  ユーザー INTEGER NOT NULL
);

DROP TABLE IF EXISTS login;
CREATE TABLE login (
  ID INTEGER PRIMARY KEY,
  email TEXT NOT NULL,
  password TEXT NOT NULL
);

INSERT INTO login (ID, email, password)
  VALUES
    (2, 'test1', 'test12');


INSERT INTO 本棚 (ID, タイトル, 内容, リンク, ユーザー)
  VALUES
    (99, 'aaaaa', 'API上限きちゃいました。', 'aaaaa', 1);

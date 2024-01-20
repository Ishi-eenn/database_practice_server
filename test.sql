DROP TABLE IF EXISTS 本棚;
CREATE TABLE 本棚 (
  ID INTEGER PRIMARY KEY,
  タイトル TEXT NOT NULL,
  内容 TEXT NOT NULL,
  リンク TEXT NOT NULL
);

DROP TABLE IF EXISTS 本;
CREATE TABLE 本 (
  ID INTEGER PRIMARY KEY,
  感想 TEXT NOT NULL
);


INSERT INTO 本棚 (ID, タイトル, 内容, リンク)
  VALUES
    (2, '進撃の巨人', 'API上限きちゃいました。', 'http://books.google.com/books/content?id=QmvVDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api');

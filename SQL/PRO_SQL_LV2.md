PROGRAMMERS LV2
=======

LINK: [PROGRAMMERS](https://school.programmers.co.kr/learn/courses/30/lessons/131120)
```
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d')AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE GENDER IN ('W') AND DATE_OF_BIRTH LIKE '_____03___' AND NOT TLNO IS NULL
ORDER BY MEMBER_ID ASC
```

LINK: [PROGRAMMERS](https://school.programmers.co.kr/learn/courses/30/lessons/131536)
```
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) >= 2
ORDER BY USER_ID ASC, PRODUCT_ID DESC
```


LINK: [PROGRAMMERS](https://school.programmers.co.kr/learn/courses/30/lessons/131115)
```
SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1
```


LINK: [PROGRAMMERS](https://school.programmers.co.kr/learn/courses/30/lessons/59038)
```
SELECT MIN(DATETIME) AS 시간
FROM ANIMAL_INS
```

LINK: [PROGRAMMERS](https://school.programmers.co.kr/learn/courses/30/lessons/59406)
```
SELECT COUNT(*) AS count
FROM ANIMAL_INS
```

LINK: [PROGRAMMERS](https://school.programmers.co.kr/learn/courses/30/lessons/59408)
```
SELECT COUNT(NAME)
FROM (SELECT DISTINCT NAME FROM ANIMAL_INS) 카운트
```
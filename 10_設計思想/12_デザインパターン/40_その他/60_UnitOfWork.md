# UnitOfWork

- Domain で起こる変更処理を都度 DB に反映させず、一連のビジネスロジックが終わったあとに Domain Model 外でまとめて反映させる方式
- DDD の Infrastructure 層に配置する
- Domain はこれを継承することになるが、Domain が Infrastructure に依存するため良くないかも？

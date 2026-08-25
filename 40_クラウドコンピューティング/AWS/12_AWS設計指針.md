# AWS設計指針

- 単一障害点(Single Point of Failure, SPOF)を避ける
  - ELB, IGWはAWSが自動で冗長化しているため、SPOFにならない
  - EC2インスタンスは冗長化されていないため、複数台構成にして冗長化する必要がある

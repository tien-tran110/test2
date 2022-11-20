# Test 2

|Token Code | Operator   |  Regex
|-----------|------------|-----------
|PLUS       |       +    |    +
|MINUS      |       -    |     -
|MUL        |      *     |     *
|DIV        |     /      |     /
|MOD        |    %       |      %
|LPARENT    |     (      |      (
|RPARENT    |       )    |     )
|LCURLB     |      {     |      {
|RCURLB     |      }     |     }
|EQ         |     =      |     =
|NE         |       !=   |      !=
|EE         |       ==   |     ==
|LT         |       <    |    <
|GT         |      >     |    >
|LTE        |     <=     |    <=
|GTE        |   >=       |    >=

Priority Order
- ( )
-  \*
-  \/
-  \%
-  \+
-  \-

Keyword Types
|Token Code| Regex   
|----------|------------
|ID        |  [_a-zA-Z]{6,8}
|START     |  START
|FINISH    | FINISH
|LOOP      |  LOOP
|SELECT    |  SELECT

Data Type 
|Name   |     Range                            |   Size      |   Regex
|-------|--------------------------------------|-------------|------------
|TX     |    -128 to 127                       |  1 byte     |   [0-9]+      
|TY     |    -32768 to 32767                   |  2 bytes    |   [0-9]+ 
|TZ     |     -2,147,483,648 to 2,147,483,647  |  4 bytes    |   [0-9]+ 
|TT     |     -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807      |   8 bytes   |  [0-9]+
      

Production rules:

- \<stmt> --> \<ifstmt> | \<while_loop> | \<as_s> | \<declaration> | \<block>
- \<block> --> START \<stmt> FINISH
- \<if_stmt> --> SELECT \<boolexpr> START \<stmt> FINISH 
- \<while_loop> --> LOOP <boolexpr> START \<stmt> FINISH
- \<ident> --> [_a-zA-Z]{6,8}
- \<as_s> --> 'id' \`=` \<expr>
- \<declaration> --> \<dtype> 'id' \`;`
- \<dtype> --> TX| TY| TZ| TT
- \<expr> --> \<term> { (\`+\`|\`-\`) \<term> }
- \<term> --> \<factor> { (\`*\`|\`/\`|\`%\`) \<factor> }
- \<factor> --> 'id' | \`(\` \<expr> \`)\`


LL Grammar:
Those production rules are LR Grammar because it is read from left to right and the recursive descent parse use 
the current input symbol to choose which path it should take. It passes the pairwise disjointness test. 


LR(1) Parser: 
Rule:

<img width="209" alt="Screenshot 2022-11-19 at 9 05 35 PM" src="https://user-images.githubusercontent.com/72286897/202879259-1fd5bb4d-a1bc-4beb-bf29-fa9eda2a6ea4.png">


-----------------

### Pass cases

<img width="536" alt="Screenshot 2022-11-19 at 8 40 16 PM" src="https://user-images.githubusercontent.com/72286897/202878687-fb549ab6-98ce-4072-aaec-61a42cb151d6.png">
<img width="399" alt="Screenshot 2022-11-19 at 8 55 09 PM" src="https://user-images.githubusercontent.com/72286897/202879024-befac8f5-7f36-496e-a11d-6bb7457ce549.png">

### Fail cases

<img width="442" alt="Screenshot 2022-11-19 at 9 01 32 PM" src="https://user-images.githubusercontent.com/72286897/202879169-780a1962-7941-4ffd-9d32-4cc529a2af29.png">
there is no rule for token '^'

<img width="262" alt="Screenshot 2022-11-19 at 9 08 56 PM" src="https://user-images.githubusercontent.com/72286897/202879325-d20efb53-82c5-4f22-ad10-bfadd1bbff1b.png">
it recognized (id as a rule instead of '(' and id separately 

# pwn_easy_admin
```
let's get the flag at /home/admin/flag !
[   nc {server } 1001   ]
```

## Solution

함수 포인터 호출 시 음수에 대한 검증은 없어 음수로 접근하여 호출할 수 있다.


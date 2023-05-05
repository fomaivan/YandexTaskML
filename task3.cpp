#include <iostream>
#include <vector>

const int M = 8;
const int N = 1'001;
const int kMod = 1'000'000'000 + 7;

int Get(int x) {
  int mask = 0;
  std::vector<int> prime_nums = {2, 3, 5, 7, 11, 13, 17, 19};
  for (int i = 0; i <= prime_nums.size() - 1; ++i) {
    while (x % prime_nums[i] == 0) {
      mask ^= (1 << i);
      x /= prime_nums[i];
    }
  }
  return mask;
}

int MultOperation(int x, int y) {
  int64_t res = static_cast<int64_t>(x) * static_cast<int64_t>(y);
  return res % kMod;
}

int Bin(int k, int tmp) {
  int res = 1;
  while (tmp > 0) {
    if (tmp % 2) {
      res = static_cast<int>(static_cast<int64_t>(res) * static_cast<int64_t>(k) % kMod);
    }
    k = static_cast<int>(static_cast<int64_t>(k) * static_cast<int64_t>(k) % kMod);
    tmp /= 2;
  }
  return res;
}

void OperationAdd(int &x, int y) {
  x += y;
  x %= kMod;
}

int dp[N][(1 << M)];

int FuncSolution(int n, int k) {
  dp[0][0] = 1;
  for (int i = 1; i < n + 1; ++i) {
    for (int j = 1; j < k + 1; ++j) {
      int new_mask = Get(j);
      int tmp = Bin(k, kMod - 2);
      for (int tmp_mask = 0; tmp_mask < (1 << M); ++tmp_mask) {
        OperationAdd(dp[i][(tmp_mask ^ new_mask)], MultOperation(dp[i - 1][tmp_mask], tmp));
      }
    }
  }

  return dp[n][0];
}

int main() {
  int n, k;
  std::cin >> n >> k;
  std::cout << FuncSolution(n, k);
}

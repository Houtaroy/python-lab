class Kmp:
    def __init__(self, b, a):
        self.a = a
        self.b = b
        # self.next = self.init_next()
        self.next = []
        self.init_next_2()

    def init_next(self):
        return [self.init_next_item(x) for x in range(len(self.a))]

    def init_next_item(self, x):
        for i in range(x, 0, -1):
            temp1 = self.a[0:i]
            temp2 = self.a[x-i+1:x+1]
            if temp1 == temp2:
                return i
        return 0

    def init_next_2(self):
        self.next.append(0)
        x = 1
        temp = 0
        while x < len(self.a):
            if self.a[temp] == self.a[x]:
                temp += 1
                x += 1
                self.next.append(temp)
            elif temp:
                temp = self.next[temp - 1]
            else:
                self.next.append(0)
                x += 1

    def search(self):
        # 当前主串位置
        tar = 0
        # 当前模式串位置, 可以理解为重复字符数
        pos = 0
        while tar < len(self.b):
            if self.b[tar] == self.a[pos]:
                tar += 1
                pos += 1
            elif pos:
                # 如果没有匹配上, 则后退一步判断之前有几位重复
                # 在重复位数继续匹配, 不用从头开始
                pos = self.next[pos - 1]
            else:
                tar += 1
            if pos == len(self.a):
                # 匹配到输出结果
                print(f'pos: {tar - pos}')
                # 后退一步继续匹配
                pos = self.next[pos - 1]


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    kmp = Kmp('ABACABACAB', 'ABAB')
    kmp.search()

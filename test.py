# 简易学生成绩管理系统
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, score):
        """添加学生和成绩"""
        self.students.append({"name": name, "score": score})
        print(f"✅ 学生 {name} 添加成功！")

    def show_all(self):
        """显示所有学生"""
        if not self.students:
            print("📭 暂无学生信息")
            return
        print("\n===== 学生成绩列表 =====")
        for i, stu in enumerate(self.students, 1):
            print(f"{i}. {stu['name']} - 分数: {stu['score']}")
        print("========================\n")

    def search_student(self, name):
        """按名字查找学生"""
        result = [s for s in self.students if s["name"] == name]
        if not result:
            print(f"🔍 未找到学生：{name}")
            return
        for s in result:
            print(f"🎯 {s['name']} 的分数是：{s['score']}")

    def get_average(self):
        """计算平均分"""
        if not self.students:
            print("📭 暂无学生数据")
            return
        avg = sum(s["score"] for s in self.students) / len(self.students)
        print(f"\n📊 班级平均分：{avg:.1f}分\n")

def main():
    sm = StudentManager()
    while True:
        print("===== 学生成绩管理系统 =====")
        print("1. 添加学生")
        print("2. 查看所有学生")
        print("3. 查询学生")
        print("4. 查看平均分")
        print("0. 退出系统")
        choice = input("请输入功能编号：")

        if choice == "1":
            name = input("输入学生姓名：")
            try:
                score = float(input("输入学生分数："))
                sm.add_student(name, score)
            except ValueError:
                print("❌ 分数必须是数字！")

        elif choice == "2":
            sm.show_all()

        elif choice == "3":
            name = input("输入要查询的姓名：")
            sm.search_student(name)

        elif choice == "4":
            sm.get_average()

        elif choice == "0":
            print("👋 退出系统，再见！")
            break

        else:
            print("⚠️ 输入无效，请重新选择！")

if __name__ == "__main__":
    main()
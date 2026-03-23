class Solution(object):
    def sortPeople(self, names, heights):
        # Tạo dictionary {height: name}
        mapping = {}
        for i in range(len(names)):
            mapping[heights[i]] = names[i]
            
        # Sắp xếp các chiều cao giảm dần
        heights.sort(reverse=True)
        
        # Dựa vào chiều cao đã sắp xếp để lấy tên tương ứng
        return [mapping[h] for h in heights]
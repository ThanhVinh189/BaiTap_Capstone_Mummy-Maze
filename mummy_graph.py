from collections import deque

class Graph:
    #? Khởi tạo bằng Hash Table
    def __init__(self, row_count, col_count):
        self.row_count = row_count
        self.col_count = col_count
        self.adjacency_list = {}
        
    """PHƯƠNG THỨC THÊM NÚT CHO BẢN ĐỒ (VERTEX)
    """
    def add_rectangle_vertex(self):
        total_vertexes = self.row_count * self.col_count 
        
        #? Tạo số lượng nút dựa trên số dòng x số cột
        for vertex in range(total_vertexes):
            self.adjacency_list[vertex] = []
            
    """PHƯƠNG THỨC THÊM CẠNH (EDGE)
    
    #? vertex1: vị trí nút bắt đầu
    #? vertex2: vị trí nút kết thúc
    
    """
    def add_edge(self, vertex1, vertex2):
        # TH1: có hướng -> thêm vertex2 vào set của vertex 1
        self.adjacency_list[vertex1].append(vertex2)
        
        # TH2: vô hướng -> thêm vertex1 vào set của vertex 2 (làm cả 2)
        self.adjacency_list[vertex2].append(vertex1)
        
    """PHƯƠNG THỨC THÊM CẠNH CHO BẢN ĐỒ (EDGE)
    """
    def add_rectangle_edges(self):
        for row in range(self.row_count):
            for col in range(self.col_count):
                # Tính giá trị của nút hiện tại
                current = row * self.col_count + col
                
                # Kiểm tra và thêm cạnh tới nút ở bên phải
                if col < self.col_count - 1:
                    self.add_edge(current, current + 1)
                    
                # Kiểm tra và thêm cạnh tới nút ở bên dưới
                if row < self.row_count - 1:
                    self.add_edge(current, current + self.col_count)

    def find_all_paths(self, start, end):
        if start < 0 :
            return False

        queue = deque([[start]])
        shortest_paths = []
        visited = set([start]) # {start}
        min_length = None

        while queue:
            path = queue.popleft()
            current = path[-1]

            for neighbor in self.adjacency_list[current]:
                if neighbor in visited and (min_length is not None and len(path) >= min_length):
                    continue
                
                new_path = list(path)
                new_path.append(neighbor)

                if neighbor == end:
                    shortest_paths.append(new_path)
                    # shortest_paths.append(new_path[1]) # for game

                    min_length = len(new_path)
                else:
                    queue.append(new_path)
                    visited.add(neighbor)
        
        return shortest_paths

    """PHƯƠNG THỨC DUYỆT VERTEX THEO CHIỀU NGANG (BREADTH-FIRST TRAVERSAL)"""
    def find_next_step(self, start, end):
        if start < 0:
            return None

        visited = set([start])
        queue = deque([[start]])
        
        # Vòng lặp duyệt đường đi đến vị trí kết thúc
        while queue:
            # curr_vertex = queue.popleft()
            path = queue.popleft()
            curr_vertex = path[-1]
            
            # Lấy danh sách nút kề (neighbor) của nút hiện tại
            for neighbor in self.adjacency_list[curr_vertex]:
                if neighbor in visited:
                    continue
                
                new_path = list(path)
                new_path.append(neighbor)
                
                # Kiểm tra đường đi đã đến được nút kết thúc chưa
                if neighbor == end:
                    return new_path[1] if len(new_path) > 1 else end
                    # return new_path
                
                # Đường đi chưa kết thúc
                queue.append(new_path)
                visited.add(neighbor)
    
#TODO: KHỞI TẠO ĐỒ THỊ MAP CHO GAME MUMMY
graph = Graph(6, 6)

graph.add_rectangle_vertex()
graph.add_rectangle_edges()

# print(graph.adjacency_list)
# print(graph.find_all_paths(1, 10))
print(graph.find_next_step(29, 1))

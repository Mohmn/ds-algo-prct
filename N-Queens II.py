
class Solution:
  
    count = 0
    
    def pos_present(self,size,pos_to_see,pos_on_watch):
        #  marks the coulmn position and row position   marks the diagonal positoin
        x_pos,y_pos = pos_on_watch
        x_len,y_len = size,size
        
        area_covered_by_pos = [[(x,y_pos) for x in range(0,size)],[(x_pos,y) for y in range(0,size)],
        [(x,y) for x,y in zip(range(x_pos-1,-1,-1),range(y_pos-1,-1,-1))],
        [(x,y) for x,y in zip(range(x_pos,x_len),range(y_pos,y_len))],
        [(x,y) for x,y in zip(range(x_pos,x_len),range(y_pos,-1,-1))],
        [(x,y) for x,y in zip(range(x_pos,-1,-1),range(y_pos,y_len))]]
       
        for array in area_covered_by_pos:
            if pos_to_see in array:
                return True
        return False
    
    def is_position_safe(self,so_far_seen,pos_to_see,size):
        if len(so_far_seen) == 0:
            return True
        else:
            for pos in so_far_seen:
                if self.pos_present(size,pos_to_see,pos):
                    # means tha pos was present in 
                    return False 
            return True
        
    def backtrack(self,row,col,safe_positions_seen_so_far,size):
        if len(safe_positions_seen_so_far) == size:
            safe_positions_seen_so_far = []
            self.count += 1
            return

        while row < size:
            while col < size:

                if self.is_position_safe(safe_positions_seen_so_far,(row,col),size):
                    safe_positions_seen_so_far.append((row,col))
                
                    self.backtrack(row,col+1,safe_positions_seen_so_far,size) #bcktrch here becasuse it will enter the recusrive function from that pos
                    safe_positions_seen_so_far.pop()
                col += 1
            row += 1
            col = 0
    def totalNQueens(self, n: int) -> int:
       
        self.backtrack(0,0,[],n)
        print(self.count)
        return self.count
        
        
        
        
        

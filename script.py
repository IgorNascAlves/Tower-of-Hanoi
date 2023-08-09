import arcade
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class TowerOfHanoi(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Tower of Hanoi")
        
        self.num_discs = 5
        self.towers = [[], [], []]
        
        for i in range(self.num_discs, 0, -1):
            self.towers[0].append(i)
        
        self.source_tower = None
        self.destination_tower = None
        
        self.move_counter = 0
        self.start_time = time.time()  # Initialize start_time here

        self.congrats_displayed = False  # Add this variable to track if congrats message is displayed

        # Define colors for the discs
        self.disc_colors = [
            arcade.color.RED,
            arcade.color.ORANGE,
            arcade.color.YELLOW,
            arcade.color.GREEN,
            arcade.color.BLUE,
            arcade.color.INDIGO,
            arcade.color.VIOLET
        ]
        
    def on_draw(self):
        arcade.start_render()
        
        for i, tower in enumerate(self.towers):
            x = (i + 1) * SCREEN_WIDTH // 4
            y = SCREEN_HEIGHT // 2
            
            for j, disc in enumerate(tower):
                disc_width = disc * 20
                disc_height = 20
                # arcade.draw_rectangle_filled(x, y + j * disc_height, disc_width, disc_height, arcade.color.BLUE)
                
                # Get the disc color based on its size
                disc_color = self.disc_colors[disc - 1]  # -1 because list indices are 0-based

                arcade.draw_rectangle_filled(x, y + j * disc_height, disc_width, disc_height, disc_color)


        if self.congrats_displayed:
            x = SCREEN_WIDTH // 2
            y = SCREEN_HEIGHT // 2

            line_height = 30  # Adjust this value to control line spacing

            lines = self.congrats_message.split('\n')
            for line in lines:
                arcade.draw_text(line, x, y, arcade.color.RED, font_size=20, anchor_x="center")
                y -= line_height
    
                
    def move_disc(self, source, destination):
        if len(self.towers[source]) == 0:
            return False
        
        if len(self.towers[destination]) == 0 or self.towers[source][-1] < self.towers[destination][-1]:
            disc = self.towers[source].pop()
            self.towers[destination].append(disc)
            self.move_counter += 1
            return True
        
        return False
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            arcade.close_window()
        if key == arcade.key.W:
            self.congrats_displayed = True
            self.congrats_message = f"Congratulations!\n You solved the puzzle in {self.move_counter} moves\n and {0:.2f} seconds."
        if key in (arcade.key.KEY_1, arcade.key.KEY_2, arcade.key.KEY_3):
            tower_index = key - arcade.key.KEY_1
            if self.source_tower is None:
                self.source_tower = tower_index
            elif self.destination_tower is None:
                self.destination_tower = tower_index
                
                if self.move_disc(self.source_tower, self.destination_tower):
                    print(f"Moved disc from tower {self.source_tower} to tower {self.destination_tower}")
                    if any(len(tower) == 0 for tower in self.towers[1:]) and all(len(tower) == 0 for tower in self.towers[0:1]):
                        elapsed_time = time.time() - self.start_time
                        print(f"Congratulations! You solved the puzzle in {self.move_counter} moves and {elapsed_time:.2f} seconds.")
                        self.congrats_displayed = True
                        self.congrats_message = f"Congratulations!\n You solved the puzzle in {self.move_counter} moves\n and {elapsed_time:.2f} seconds."

                else:
                    print("Invalid move!")
                    
                self.source_tower = None
                self.destination_tower = None
        
        # Additional key options
        if key == arcade.key.R:
            self.reset_game()
            
    def reset_game(self):
        self.towers = [[], [], []]
        for i in range(self.num_discs, 0, -1):
            self.towers[0].append(i)
        self.move_counter = 0
        self.start_time = time.time()
        self.congrats_displayed = False
        print("Game reset.")
                
def main():
    window = TowerOfHanoi()
    arcade.run()

if __name__ == "__main__":
    main()

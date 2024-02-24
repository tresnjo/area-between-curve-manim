from manim import *

class integral_diff(MovingCameraScene):
    
    def construct(self):
        
        # Defining a grid
        x_min = 0
        x_max = 2
        delta_x = 0.5

        grid = Axes(
            x_range=[x_min, x_max, delta_x], 
            y_range=[x_min, x_max, delta_x],
            x_length=9,
            y_length=5.5,
            axis_config={
                "font_size": 24,
                "include_numbers":True
            },
            tips=False,
        )

        # Function 1
        plot_1 = grid.plot(
                lambda x: x**2, color=MAROON_A, use_smoothing=False)
        area_1 = grid.get_area(plot_1, x_range=(0,1)).set_color(MAROON_A)
        
        # Function 2
        plot_2 = grid.plot(
                lambda x: np.sqrt(x), color=MAROON_A, use_smoothing=False)
        area_2 = grid.get_area(plot_2, x_range=(0,1)).set_color(MAROON_A)
        
        # Difference, first mentioned is the upper function, second mentioned is the lower function
        diff_region = Difference(area_2, area_1, color = MAROON_A, fill_opacity = 0.8)  

        # Animating the result
        self.play(FadeIn(grid))
        self.wait(1)

        self.play(FadeIn(plot_1))
        self.wait(1)

        self.play(FadeIn(plot_2))
        self.wait(1)
        
        self.play(Write(diff_region))
        self.wait(1)

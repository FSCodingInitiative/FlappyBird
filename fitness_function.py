class fitness:

    def read_out_coords(pipe_coords):
        x_dists = []
        ytop_dists = []
        ybot_dists = []
        for i in pipes_coords:
            x, yt, yb = i
            x_dists.append(x)
            ytop_dists.append(yt)
            ybot_dists.append(yb)
        return x_dists, ytop_dists, ybot_dists

    
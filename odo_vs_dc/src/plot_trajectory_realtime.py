#!/usr/bin/env python3
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import rospy
from geometry_msgs.msg import Point

class TrajectoryPlotter:
    def __init__(self):
        rospy.init_node('plot_trajectory_xy', anonymous=True)
        self.data = {
            '/gt': {'x': [], 'y': []},
            '/odo': {'x': [], 'y': []},
            '/dr': {'x': [], 'y': []},
            '/odo_husky': {'x': [], 'y': []}
        }
        rospy.Subscriber('/gt', Point, self.callback, callback_args='/gt')
        rospy.Subscriber('/odo', Point, self.callback, callback_args='/odo')
        rospy.Subscriber('/dr', Point, self.callback, callback_args='/dr')
        rospy.Subscriber('/odo_husky', Point, self.callback, callback_args='/odo_husky')

        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        
        # Legendas atualizadas conforme sua solicitação
        self.ln_gt, = plt.plot([], [], 'b-', label='Ground Truth')
        self.ln_odo, = plt.plot([], [], 'r--', label='Odometria Cinemática')
        self.ln_dr, = plt.plot([], [], 'c-', label='Dead Reckoning', linewidth=2)
        self.ln_husky, = plt.plot([], [], 'm-', label='Husky Odometria', alpha=0.5)

    def callback(self, msg, topic):
        self.data[topic]['x'].append(msg.x)
        self.data[topic]['y'].append(msg.y)

    def init_plot(self):
        self.ax.set_title('Trajetoria em Tempo Real - Plano XY')
        self.ax.set_xlabel('X (m)')
        self.ax.set_ylabel('Y (m)')
        self.ax.legend()
        self.ax.grid(True)
        
        # Mantendo os limites que definimos para estabilidade
        self.ax.set_xlim([-15, 15])
        self.ax.set_ylim([-30, 10])
        
        return self.ln_gt, self.ln_odo, self.ln_dr, self.ln_husky

    def update_plot(self, frame):
        self.ln_gt.set_data(self.data['/gt']['x'], self.data['/gt']['y'])
        self.ln_odo.set_data(self.data['/odo']['x'], self.data['/odo']['y'])
        self.ln_dr.set_data(self.data['/dr']['x'], self.data['/dr']['y'])
        self.ln_husky.set_data(self.data['/odo_husky']['x'], self.data['/odo_husky']['y'])
        
        return self.ln_gt, self.ln_odo, self.ln_dr, self.ln_husky

if __name__ == '__main__':
    plotter = TrajectoryPlotter()
    ani = FuncAnimation(plotter.fig, plotter.update_plot, init_func=plotter.init_plot, blit=True, interval=100)
    plt.show()
    rospy.spin()

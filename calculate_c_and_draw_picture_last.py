import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

def read_data(file_name,sheet_name):
    df_data = pd.read_excel(file_name,sheet_name)
    return df_data.values

def calculate_pave(data,diff_time,total_time):
    num_points = len(data)
    sum_p=np.zeros(num_points)
    for num in range(num_points):
        sum_p[num] = np.sum(data[num,3,:]*diff_time)
    return sum_p/total_time

def calculate_c(data,p_ave,total_time_step):
    rho = 997
    u = 61.7847*(1165/2*10**-3)
    c = np.zeros((len(p_ave),total_time_step))
    for num_points in range(len(p_ave)):
        c[num_points,:] = (data[num_points,3,:] - p_ave[num_points])/(0.5*rho*u**2)
    return c

#时域图

def draw_shiyu(total_time,c_r,file_name):
    fig = plt.figure(figsize=(4,3))
    ax = Axes3D(fig)
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    points_num = len(c_r[:,0])
    tick_label_name = []
    for i in range(points_num):
        tick_label = np.ones(len(c_r[0,39:-1]))*i+1
        ax.plot(total_time[40:-1],tick_label,c_r[i,39:-1],linewidth=1)
        tick_label_name.append('%d'%i)
    plt.xlim(total_time[40],total_time[-2])
    if file_name == 'sump':
        ax.set_yticks(np.arange(1,points_num+1))  
    if file_name == 'blade':
        ax.set_yticks(np.arange(1,points_num+1,2)) 
    ax.set_zlabel(r'${C^*}$',fontsize=10.5)
    ax.set_ylabel('点下标序数',fontsize=10.5,fontfamily="simsun")
    ax.set_xlabel('t/s',fontsize=10.5)
    save_file_name = r'D:\zgh\study\fourth_grade\graduate_design\document\picture\calculate\transient_pressure' + '\\' + file_name + '_t_C.svg'
    plt.savefig(save_file_name,dpi=1000,format='svg',bbox_inches='tight')
'''
def draw_shiyu(total_time,c_r,file_name):
    plt.figure(figsize=(5,3.75))
    points_num = len(c_r[:,0])
    for i in range(points_num):
        plt.plot(total_time[1:-1],c_r[i,0:-1],label='p%d'%(i+1),linewidth=1)
    plt.xlim(total_time[1],total_time[-2]) 
    plt.ylabel(r'${C^*}$',fontsize=10.5)
    plt.xlabel('t/s',fontsize=10.5)
    save_file_name = r'D:\zgh\study\fourth_grade\graduate_design\document\picture\calculate\transient_pressure' + '\\' + file_name + '_t_C.svg'
    plt.savefig(save_file_name,dpi=1000,format='svg',bbox_inches='tight')    
'''  

#频域图
def draw_pinyu(total_time,c_r,file_name):
    fig = plt.figure(figsize=(4,3))
    ax = Axes3D(fig)
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    #ax.grid(False)
    f_T = 590/60
    tick_label_name = []
    points_num = len(c_r[:,0])
    for i in range(points_num):
        c_r_cal = c_r[i,40:-1]
        fft_re = np.fft.fft(c_r_cal)
        fre = np.fft.fftfreq(c_r_cal.size,total_time[2]-total_time[1])/f_T
        pow = np.abs(fft_re)/(len(c_r_cal)/2)
        tick_label = np.ones(len(fre[fre>0]))*i +1
        ax.plot(fre[fre > 0],tick_label,pow[fre > 0],linewidth=1)
        tick_label_name.append('%d'%i)
    if file_name == 'sump':
        ax.set_yticks(np.arange(1,points_num+1))  
    if file_name == 'blade':
        ax.set_yticks(np.arange(1,points_num+1,2)) 
    ax.set_zlabel(r'${C^*}$',fontsize=10.5)
    ax.set_ylabel('点下标序数',fontsize=10.5,fontfamily="simsun")
    ax.set_xlabel(r'${f/f_T}$',fontsize=10.5)
    #plt.tight_layout()
    save_file_name = r'D:\zgh\study\fourth_grade\graduate_design\document\picture\calculate\transient_pressure' + '\\' + file_name + '_fft.svg'
    plt.savefig(save_file_name,dpi=1000,format='svg',bbox_inches='tight')
            




def main():
    total_time_step = 81
    #数组初始化
    sump_data = np.zeros((3,4,total_time_step))
    blade_data = np.zeros((14,4,total_time_step))
    volute_data = np.zeros((23,4,total_time_step))
    #时间列表
    every_time_step = 0.000847458
    total_time = np.array([0.00169492+each*3*every_time_step for each in range(total_time_step-1)])
    total_time = np.insert(total_time,0,0)
    total_time = np.append(total_time,0.20339)
    diff_time = np.diff(total_time)
    #读取压力文件
    sheet_first_name = 'time_'
    for sheet_index in range(total_time_step):
        sheet_name = sheet_first_name + str(sheet_index)
        blade_data[:,:,sheet_index] = read_data(r'.\data\blade.xlsx',sheet_name)
        sump_data[:,:,sheet_index] = read_data(r'.\data\sump.xlsx',sheet_name)
        volute_data[:,:,sheet_index] = read_data(r'.\data\volute.xlsx',sheet_name)
    #计算时均压力pave
    blade_pave = calculate_pave(blade_data,diff_time,total_time[-1])
    sump_pave = calculate_pave(sump_data,diff_time,total_time[-1])
    volute_pave = calculate_pave(volute_data,diff_time,total_time[-1])
    #计算C*
    blade_c = calculate_c(blade_data,blade_pave,total_time_step)
    sump_c = calculate_c(sump_data,sump_pave,total_time_step)
    volute_c = calculate_c(volute_data,volute_pave,total_time_step)

    #调整顺序
    index_blade = np.array([2,1,4,6,8,12,10,3,5,7,13,14,11,9]) - 1
    index_sump = np.array([3,2,1]) - 1
    index_volute = np.array([23,22,21,9,8,11,10,13,12,15,14,17,16,20,19,18,1,2,3,4,5,6,7]) - 1

    blade_c = blade_c[index_blade,:]
    sump_c = sump_c[index_sump,:]
    volute_c = volute_c[index_volute,:]
    #print(blade_c[0,:])

    
    draw_shiyu(total_time,volute_c,'volute')
    draw_pinyu(total_time,volute_c,'volute')
    draw_shiyu(total_time,blade_c,'blade')
    draw_pinyu(total_time,blade_c,'blade')
    draw_shiyu(total_time,sump_c,'sump')
    draw_pinyu(total_time,sump_c,'sump')
    #fft
   
 
if __name__ == '__main__':
    main()
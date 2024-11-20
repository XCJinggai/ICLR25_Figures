### Clic数据集  --》 JPEG框架
### 参照的方法画上，虚线
### 原JPEG和移动后的JPEG

import matplotlib.pyplot as plt
import seaborn as sns

# 设置样式
sns.set(style="whitegrid")

# plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['axes.linewidth'] = 1   # 边框线宽
plt.rcParams['xtick.major.width'] = 1   # x轴刻度线宽
plt.rcParams['ytick.major.width'] = 1  # y轴刻度线宽
plt.rcParams['xtick.labelsize'] = 18  # x轴刻度字体大小
plt.rcParams['ytick.labelsize'] = 18  # y轴刻度字体大小

# 数据

bmshjfactor_2048_bps = [
    0.065,
    0.099,
    0.148,
    0.221,  #
    0.321,
    0.511,
    0.768,
    1.161
]

bmshjfactor_4096_bps = [
    0.0487,
    0.0737,
    0.112,
    0.169,  #
    0.249,
    0.401,
    0.623,
    0.961

]

bmshjfactor_8192_bps = [
    0.0387,
    0.0593,
    0.0886,
    0.135,  # 
    0.196,
    0.322,
    0.526,
    0.851

]

bmshjfactor_bps = [
    0.106,
    0.157,
    0.232,
    0.343,
    0.496,
    0.736,
    1.050,
    1.467

]
bmshjfactor_distortion = [
    28.97,
    30.31,
    31.66,
    33.14,
    34.57,
    36.50,
    38.20,
    40.07

 ]

bmshjhyper_bps =  [
      0.10714188654859463,
      0.16155050770553617,
      0.23953942078204957,
      0.3511461665024439,
      0.49252192177516946,
      0.706258013649693,
      0.9828958591060444,
      1.3368811140083006
    ]
bmshjhyper_distortion =[
      29.441001612965653,
      30.973992696622524,
      32.56758680576232,
      34.20097509244593,
      35.62152890461247,
      37.46330363576005,
      38.94454146594536,
      40.7391953817228
    ] 


origin_jpeg_bps = [
0.26942240963756375,   #10
0.40312596713998394,  #20
0.5177685074622211,  #30
0.6160570990964902, #40
0.8173946247987677, #60
1.2576960108254909,  #80
1.93194318967267,     #90
2.897694796647583,  #95
     ]
moved_jpeg_bps =  [
0.0836421,
0.166850,
0.238016,
0.297502,
0.404581,
0.5908798,
0.953877,
1.46357,
     ] 
jpeg_distortion = [
    28.14758265443904,
    30.65092614075012,
    31.90639323358514,
    32.73495553262414,
    34.01572012087114,
    36.03780639790182,
    38.15409381992603,
    40.36549841495102,
    ]

cheng20_bps = [
      0.0873912191517858,
      0.12901223799906825,
      0.19462149259271955,
      0.3078033992480054,
      0.4267893794458668,
      0.584461365405017
    ]
cheng20_distortion =  [
      30.181455658703314,
      31.520532096304546,
      32.945748026778055,
      34.669439687961486,
      35.94880894916813,
      37.34391598585175
    ]

xie21_bps = [
        0.07203977324678053,
        0.09755356726631553,
        0.11748815950460842,
        0.20864437863241664,
        0.31829253667507795,
        0.45920202148814876,
        0.564088358437684,
        0.7759934857000356
      ]
xie21_distortion =  [
        29.59623646173013,
        30.620305225841804,
        31.368097891084776,
        33.500982263908604,
        35.1986092737886,
        36.75209027231476,
        37.659769404047275,
        38.98167890128869
      ]

mlicpp_bps = [
      0.0799, 
      0.128, 
      0.1954, 
      0.3037, 
      0.4274, 
      0.5879
    ]
mlicpp_distortion = [
      31.0686, 
      32.5063, 
      33.9165, 
      35.4683, 
      36.8134, 
      38.0922
    ]

fat_bps = [
      0.105,
      0.155,
      0.225,
      0.322,
      0.451,
      0.627
    ]
fat_distortion =   [
      31.38,
      32.83,
      34.23,
      35.69,
      37.15,
      38.64
    ]

vtm_bps =  [
      0.028693439,
      0.065975472,
      0.14522685,
      0.292789702,
      0.548178569,
      0.69374136
    ]
vtm_distortion =  [
      27.47951725,
      29.76164242,
      32.21946528,
      34.78378193,
      37.39918862,
      38.441893
    ]

hm_bps = [
      0.074666,
      0.124894,
      0.173318,
      0.361170,
      0.527422,
      0.761656
    ]
hm_distortion =  [
      28.996752,
      30.374770,
      31.419636,
      34.138789,
      35.845424,
      37.569206
    ]

TCM_bps = [
    0.117,
    0.144,
    0.216,
    0.315,
    0.447,
    0.641,
    ]

TCM_distortion = [
    31.97,
    32.70,
    34.15,
    35.65,
    37.14,
    38.75,
    ]

# 创建图形
plt.figure(figsize=(8,6))

# 设置边框颜色
for spine in plt.gca().spines.values():
    spine.set_color('black')  # 设置边框为黑色

# 设置主刻度和次刻度的颜色和线宽
plt.tick_params(axis='x', which='both', direction='in', length=6, width=1, colors='black')
plt.tick_params(axis='y', which='both', direction='in', length=6, width=1, colors='black')

# 使刻度线更具可见性，添加次刻度
plt.minorticks_on()
plt.tick_params(axis='both', which='minor', length=4, color='gray')

# # 绘制曲线
plt.plot(origin_jpeg_bps, jpeg_distortion,  marker='o', label='JPEG', color='green')
plt.plot(moved_jpeg_bps, jpeg_distortion,  marker='s', label='Ours + JPEG', color='green')
plt.plot(bmshjfactor_bps, bmshjfactor_distortion,  marker='o', label='FactorizedPrior', color='blue')
# plt.plot(bmshjfactor_2048_bps, bmshjfactor_distortion,   marker='s', label='Ours + FP(2048)', color='#6495ED')
# plt.plot(bmshjfactor_4096_bps, bmshjfactor_distortion,   marker='s', label='Ours + FP(4096)', color='#4169E1')
plt.plot(bmshjfactor_8192_bps, bmshjfactor_distortion,   marker='s', label='Ours + FactorizedPrior', color='blue')
plt.plot(bmshjhyper_bps, bmshjhyper_distortion,  linestyle="--", marker='', label='HyperPrior', color='black')
plt.plot(hm_bps, hm_distortion,  linestyle="--", marker='', label='HM', color='pink')
plt.plot(cheng20_bps, cheng20_distortion,  linestyle="--", marker='', label='Cheng20', color='orange')
plt.plot(xie21_bps, xie21_distortion,  linestyle="--", marker='', label='Xie21', color='brown')
plt.plot(vtm_bps, vtm_distortion,  linestyle="--", marker='', label='VTM', color='red')
plt.plot(fat_bps, fat_distortion,  linestyle="--", marker='', label='FAT', color='magenta')
plt.plot(TCM_bps, TCM_distortion,  linestyle="--", marker='', label='TCM', color='gray')
plt.plot(mlicpp_bps, mlicpp_distortion,  linestyle="--", marker='', label='MLIC++', color='cyan')


# 启用网格并设置次刻度网格
plt.grid(True, which='both')  # 显示主刻度和次刻度的网格线
plt.minorticks_on()  # 启用次刻度
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')  # 调整次刻度网格线的样式
plt.title('Performance on CLIC',fontsize=20,color="black")

# 设置轴标签
plt.xlabel('bits per pixel (bpp)', fontsize=20)
plt.xlim(0,1.5)
plt.ylabel('PSNR (dB)', fontsize=20)
plt.ylim(27.9,40.5)

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# 设置图例
plt.legend(ncol=2 ,loc='lower right',fontsize=15)

# 去除留白
plt.tight_layout()

# 保存为 PDF
plt.savefig('Figure5b.pdf', format='pdf',)


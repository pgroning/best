import matplotlib.patches as mpatches
from main_gui import Circle
import numpy as np

def s96o2(self):
    
    # Draw water cross
    # West
    pp = [[0.088, 0.503], [0.15, 0.515], [0.3, 0.515], [0.36, 0.503], [0.38, 0.503],
          [0.38, 0.497], [0.36, 0.497], [0.3, 0.485], [0.15, 0.485], [0.088, 0.497]]
    poly = mpatches.Polygon(pp)
    poly.set_facecolor((0.8,0.898,1))
    poly.set_linewidth(1.5)
    poly.set_closed(False)
    self.axes.add_patch(poly)
    # East
    pp = [[0.922, 0.503], [0.86, 0.515], [0.71, 0.515], [0.65, 0.503], [0.63, 0.503],
          [0.63, 0.497], [0.65, 0.497], [0.71, 0.485], [0.86, 0.485], [0.922, 0.497]]
    poly = mpatches.Polygon(pp)
    poly.set_facecolor((0.8,0.898,1))
    poly.set_linewidth(1.5)
    poly.set_closed(False)
    self.axes.add_patch(poly)
    # South
    pp = [[0.497, 0.088], [0.485, 0.15], [0.485, 0.3], [0.497, 0.36], [0.497, 0.38],
        [0.503, 0.38], [0.503, 0.36], [0.515, 0.3], [0.515, 0.15], [0.503, 0.088]]
    poly = mpatches.Polygon(pp)
    poly.set_facecolor((0.8,0.898,1))
    poly.set_linewidth(1.5)
    poly.set_closed(False)
    self.axes.add_patch(poly)
    # North
    pp = [[0.497, 0.922], [0.485, 0.86], [0.485, 0.71], [0.497, 0.65], [0.497, 0.63],
          [0.503, 0.63], [0.503,0.65], [0.515, 0.71], [0.515, 0.86], [0.503, 0.922]]
    poly = mpatches.Polygon(pp)
    poly.set_facecolor((0.8,0.898,1))
    poly.set_linewidth(1.5)
    poly.set_closed(False)
    self.axes.add_patch(poly)


    # Draw water channel
    # Rectangle center at origo
    rect = mpatches.Rectangle((-0.095,-0.095), 0.19, 0.19, fc=(0.8,0.898,1),ec=(0.3, 0.3, 0.3))
    rect.set_linewidth(2.0)
    # 1. Translate rectangle along x-axis a distance 1/sqrt(2).
    # 2. Rotate 45 degrees
    rot45=mpatches.transforms.Affine2D().rotate_deg(45) + self.axes.transData
    transrot = mpatches.transforms.Affine2D().translate(0.70711,0.0) + rot45#self.axes.transData
    rect.set_transform(transrot)

    self.axes.add_patch(rect)


    # Draw enrichment levels
    case_num = int(self.case_cbox.currentIndex())
    FUE = self.dataobj.cases[case_num].data.FUE
    enr_levels  = FUE[:,2]
    enr_ba = FUE[:,4]
    #print enr_levels, enr_ba
 
    cmap = ["#6666FF","#B266FF","#66FFFF","#00CC00","#66FF66","#FFFF66","#FFB266","#FF9999","#FF3333","#FF3399"]
    #cmap = [[0,0,1], [0,1,1], [0,1,0], [0.604,0.804,0.196], [1,1,0], [0.933,0.867,0.51], [1,0.549,0], [1,1,1], [1,0,0]]
    #enr_steps = [0.71, 2.5, 3.2, 3.4, 4.0, 4.2, 4.6, 4.9, 0]
    #enr_ba = [3.4, 5.0]

    pin_radius = 0.028
    pin_delta = 0.078
    
    # Draw enrichment level circles
    self.enrpinlist = []
    x = 1.06
    for i in range(enr_levels.size):
        y = 0.9-i*pin_delta
        circobj = Circle(self.axes,x,y,cmap[i],str(i+1))
        self.axes.text(x+0.05,y,"%.2f" % enr_levels[i],fontsize=8)
        circobj.ENR = enr_levels[i]
        circobj.BA = enr_ba[i]
        if not np.isnan(enr_ba[i]):
            circobj.set_text('Ba')
            self.axes.text(x+0.05,y-0.03,"%.2f" % enr_ba[i],fontsize=8)
            
        self.enrpinlist.append(circobj)

    # Print average enrichment
    ave_enr = self.dataobj.cases[case_num].data.ave_enr
    self.axes.text(1.02,0.05,"%.3f %%U-235" % ave_enr,fontsize=8)
    
    # Draw pin circles
    npst = self.dataobj.cases[case_num].data.npst
    LFU = self.dataobj.cases[case_num].data.LFU
    # Remove water cross
    LFU = np.delete(LFU, (5), axis=0) # Delete row 6
    LFU = np.delete(LFU, (5), axis=1) # Delete col 6
    #i = [i for i in range(LFU.shape[0]) if np.all(LFU[i,:]==0)][0]
    #j = [j for j in range(LFU.shape[1]) if np.all(LFU[:,j]==0)][0]

    self.circlelist = []
    for i in range(LFU.shape[0]):
        for j in range(LFU.shape[1]):
            x = 0.13+j*pin_delta
            y = 0.87-i*pin_delta
            if j > 4: x += 0.04
            if i > 4: y -= 0.04
            if LFU[i,j] > 0:
                circobj = Circle(self.axes,x,y,(1,1,1),'')
                circobj.coord = self.ylist[i] + self.xlist[j]
                self.circlelist.append(circobj)

                
    # Draw pin coordinates x-axis
    for i in range(5):
        self.axes.text(0.13+i*pin_delta,0.015,self.xlist[i],ha='center',va='center',fontsize=9)
    for i in range(5,10):
        self.axes.text(0.17+i*pin_delta,0.015,self.xlist[i],ha='center',va='center',fontsize=9)
        
    # Draw pin coordinates y-axis
    for i in range(5):
        self.axes.text(0.99,0.87-i*pin_delta,self.ylist[i],ha='center',va='center',fontsize=9)
    for i in range(5,10):
        self.axes.text(0.99,0.83-i*pin_delta,self.ylist[i],ha='center',va='center',fontsize=9)
        
        #self.canvas.draw()
        #Tracer()()

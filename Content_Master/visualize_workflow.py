import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch

def create_workflow_diagram():
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    
    nodes = [
        ("Query Analyzer", 2, 9),
        ("Research Agent", 2, 7.5),
        ("Source Verifier", 2, 6),
        ("Content Planner", 2, 4.5),
        ("Content Generator", 2, 3),
        ("Visual Creator", 0.5, 1.5),
        ("Template Selector", 3.5, 1.5),
        ("Content Assembler", 2, 0)
    ]
    
    for name, x, y in nodes:
        box = FancyBboxPatch((x-0.6, y-0.3), 1.2, 0.6, 
                           boxstyle="round,pad=0.1", 
                           facecolor='lightblue', 
                           edgecolor='navy')
        ax.add_patch(box)
        ax.text(x, y, name, ha='center', va='center', fontsize=9, weight='bold')
    
    edges = [
        (2, 9, 2, 7.8),
        (2, 7.2, 2, 6.3),
        (2, 5.7, 2, 4.8),
        (2, 4.2, 2, 3.3),
        (1.7, 2.7, 0.8, 1.8),
        (2.3, 2.7, 3.2, 1.8),
        (0.5, 1.2, 1.4, 0.3),
        (3.5, 1.2, 2.6, 0.3)
    ]
    
    for x1, y1, x2, y2 in edges:
        ax.arrow(x1, y1, x2-x1, y2-y1, head_width=0.05, head_length=0.05, 
                fc='black', ec='black')
    
    ax.text(1, 8, "Retry if\ninsufficient", fontsize=8, ha='center', color='red')
    ax.text(3.2, 5.2, "Retry if\nlow quality", fontsize=8, ha='center', color='red')
    ax.text(0.5, 2.5, "If needs\nvisuals", fontsize=8, ha='center', color='green')
    ax.text(3.5, 2.5, "If text\nonly", fontsize=8, ha='center', color='green')
    
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('ContentMaster LangGraph Workflow', fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('workflow_diagram.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    create_workflow_diagram() 
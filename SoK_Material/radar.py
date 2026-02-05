import matplotlib.pyplot as plt
import numpy as np

labels = [
    'CL1\nData\nBinding',
    'CL2\nTraining\nCorrectness',
    'CL3\nUpdate\nAdmissibility',
    'CL4\nUniqueness',
    'AG1\nCorrect\nAdmission',
    'AG2\nCorrect\nAggregation',
    'AG3\nNon-\nEquivocation'
]
num_vars = len(labels)

# Frequency: Normalized to 0-5 scale
MAX_VAL = 5
data_frequency = [x / 2.0 for x in [2, 6, 5, 1, 2, 10, 3]]

raw_complexity = [1.0, 4.0, 2.0, 0.0, 0.5, 3, 0]
data_feasibility = [5.0 - x for x in raw_complexity]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

data_frequency += data_frequency[:1]
data_feasibility += data_feasibility[:1]

fig, ax = plt.subplots(figsize=(14, 14), subplot_kw=dict(polar=True))

ax.set_theta_offset(np.pi / 2 + 5 * 2 * np.pi / num_vars)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], labels, color='#333333', size=20, weight='bold')
ax.tick_params(axis='x', pad=18)
for lbl in ax.get_xticklabels():
    lbl.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.85, pad=3))

ax.set_rlabel_position(0)
plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=9)
plt.ylim(0, 5.5)

circle_angles = np.linspace(0, 2 * np.pi, 100)
for r in [1, 2, 3, 4, 5]:
    ax.plot(circle_angles, [r] * len(circle_angles), color='#525252', linewidth=0.5, alpha=0.5)

ax.plot(angles, data_frequency, linewidth=2, linestyle='-', color='#007acc', label='Research focus (0 = none, 5 = highest)')
ax.fill(angles, data_frequency, '#007acc', alpha=0.2)

ax.plot(angles, data_feasibility, linewidth=2, linestyle='--', color='green', label='Ease of implementation (0 = hardest, 5 = trivial)')


ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.28), frameon=False, fontsize=21, ncol=1, labelspacing=0.8)
#plt.title('Research focus vs. Technical feasibility',
#          size=16, weight='bold', y=1.08)


plt.tight_layout(pad=2.0)
plt.savefig('out/vfl_radar_comparison_feasibility.png')
plt.show()

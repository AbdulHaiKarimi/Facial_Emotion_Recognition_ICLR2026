from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Recent Progress in Deep Learning (DL) has shown that data quality constrains the generalization as much as model design. Facial Emotion Recognition (FER) exemplifies this challenge, as widely used datasets contain mislabeled, duplicated, class imbalanced, and visually affected samples that weaken both accuracy and robustness. In this paper we proposed a data-centric approach to FER, building a systematic pipeline that improves dataset reliability before model training. The pipeline includes (i) Noisy and duplicated samples removal, (ii) landmark-guided facial refinement, and (iii) class-aware re-balanced under-presented emotions in the dataset. Following the data-centric pipeline we proposed a lightweight hybrid CNN-Transformer student model with Emotion Aware Dynamic Distillation (EADD), where knowledge is adaptively distilled from multiple teacher networks depending on their emotion-specific strengths. Despite the multi-teacher knowledge distillation student model is further optimized by adversarial training to enhance its robustness against subtle perturbations in real-world FER. Extensive experiments on FER2013 and KDEF highlights that our approach achieved state-of-the-art robustness, efficiency and trade-offs for real-time FER on Edge devices. The results demonstrate that systematic data refinement is as critical as model innovation.',
    author='Abdul Hai Karimi',
    license='MIT',
)

import os
from setuptools import find_packages, setup
from typing import List

_PATH_ROOT = os.path.realpath(os.path.dirname(__file__))


def _load_requirements(path_dir: str, file_name: str = "requirements.txt", comment_char: str = "#") -> List[str]:
    with open(os.path.join(path_dir, file_name)) as f:
        lines = [line.strip() for line in f.readlines()]
    requirements = []
    for line in lines:
        if comment_char in line:
            char_idx = min(line.index(ch) for ch in comment_char)
            line = line[:char_idx].strip()
        if line:
            requirements.append(line)
    return requirements


BASE_REQUIREMENTS = _load_requirements(_PATH_ROOT)


setup(
    name="nlg_eval_via_simi_measures",
    version="0.1.0dev",
    url="https://github.com/PierreColombo/nlg_eval_via_simi_measures",
    author="Pierre Colombo, Guillaume Staerman",
    author_email="pierre.colombo@centralesupelec.fr, guillaume.staerman@telecom-paris.fr",
    short_description="Automatic evaliation NLG metrics.",
    packages=find_packages(),
    keywords=["natural language generation", "evaluation", "metrics"],
    python_requires=">=3.6",
    install_requires=BASE_REQUIREMENTS,
    classifiers=[
        "Environment :: Console",
        "Natural Language :: English",
        # How mature is this project? Common values are
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        "Development Status :: 4 - Beta",
        "Intended Audience :: Researchers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={"console_scripts": ["nlg-score-cli = nlg_eval_simi_measures.score_cli:main"]},
)

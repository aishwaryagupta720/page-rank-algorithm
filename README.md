# PageRank Algorithm Implementation

## Project Overview
This project is an implementation of the PageRank algorithm, which ranks web pages based on their link structure. The algorithm calculates the importance of each page by simulating a random web surfer who randomly clicks on links, with a probability of teleporting to a random page.

## Features
- **Graph Parsing:** Reads graph data from an input text file.
- **Sparse Matrix Construction:** Converts the graph into a sparse matrix representation.
- **Power Iteration Method:** Computes PageRank values iteratively until convergence.
- **Teleportation Mechanism:** Handles dead ends and disconnected components.

## File Structure
- `PageRank.py`: Main script containing the implementation.
- `input.txt`: Example input file encoding the web graph.
- `output.txt`: Output file with the PageRank values.

## Installation and Usage

### Prerequisites
- Python 3.x
- NumPy
- SciPy

Install the necessary packages:
```bash
pip install numpy scipy
```

### Running the Code
Run the algorithm with:
```bash
python PageRank.py input.txt 0.85 > output.txt
```
Replace `0.85` with your desired damping factor.

### Output
The program outputs the PageRank values in scientific notation, with 10 decimal places, one per line for each vertex.

## Experimentation
The project includes functionality to test various damping factors (from 0.75 to 0.95 in increments of 0.05) and analyze convergence and rank distribution.

## Results Summary
- Convergence achieved in about 10-11 iterations.
- Higher damping factors increase the top PageRank values, concentrating rank among highly linked nodes.

## Acknowledgments
This project is part of the CSEN 272 Web Search and Information Retrieval course.

## Author
Aishwarya Gupta

For more details, see the project report.

---

Let me know if you want any adjustments or additional sections! 🚀


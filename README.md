

<br />
<p align="center">

  <h3 align="center">Graph Traversal Visualization Tool</h3>


  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project
![photo1]
This is a simple python application in which you pick a start square and an end square from a 50 by 50 grid (changable in the code), and place barriers in between those points at any square the user wishes to. By pressing spacebar after the user is done drawing his\hers start, end and barrier points, the A* algorithm begins. On the screen you will be able to see the computer traversing through the grid in an a* fashion. A blue square will indicate the starting position while an orange one indicates the end square. If a square is turned green it means this square was pushed to the Priority Queue (PQ) from which the algorithm chooses its next node to inquire. The red squares are squares which have already been investigated and found not to be equal to the end node (i.e. closed nodes).

![photo2]
### Built With

* [pygame](https://www.pygame.org/docs/)
* [Python 3.7.1](https://www.python.org/downloads/release/python-371/)





## Prerequisites

Just install pygame 1.9.6:
              pip install pygame==1.9.6


## Usage
Simply run the program and choose the stat square and the end square subsequently, choose barrier. IF you wan to erase a square (i.e. change the start\end\barrier points), simply right click on the chosen square. If you erase a start\end\barrier square, the next time you will click on a square it will turn to the same type of square you have just deleted. 



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact
Project Link: [https://github.com/nadavleh/Chess_AI](https://github.com/nadavleh/Chess_AI)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/nadavleh/repo.svg?style=flat-square
[forks-shield]: https://img.shields.io/github/forks/nadavleh/repo.svg?style=flat-square
[forks-url]: https://github.com/nadavleh/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/nadavleh/repo.svg?style=flat-square
[stars-url]: https://github.com/nadavleh/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/nadavleh/repo.svg?style=flat-square
[issues-url]: https://github.com/nadavleh/repo/issues
[license-shield]: https://img.shields.io/github/license/nadavleh/repo.svg?style=flat-square
[photo1]: https://github.com/nadavleh/Graph-Traversal-Visualization-Tool/blob/main/graph1.png
[photo2]: https://github.com/nadavleh/Graph-Traversal-Visualization-Tool/blob/main/graph2.png

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<a href="https://github.com/dinobenj/GlacierProject">
<img src="https://github.com/dinobenj/GlacierProject/blob/main/glacierProjectLogo.png" alt="Glacier Project Logo" width="360" height="216">
</a>
<h3 align="center">Glacier Project</h3>


  <p align="center">
    The Glacier Project is a web application that visualizes data, satellite images, and predictions of our planet's glaciers.
    <br />
    <a href="https://github.com/dinobenj/GlacierProject"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dinobenj/GlacierProject">View Demo</a>
    ·
    <a href="https://github.com/dinobenj/GlacierProject">Report Bug</a>
    ·
    <a href="https://github.com/dinobenj/GlacierProject">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About 

Current Features include:

 * Filtering by country and displaying the location of a glacier on a map 
 * Displaying mass change data based on recordings by the WGMS 
 * Downloading CSV files of data 
 * Displaying raster plots of the elevation in a small area around a glacier




### Built With

* [![React][React.js]][React-url]
* [![Typescript][Typescript.com]][Typescript-url]
* [![R Shiny][RShiny.com]][RShiny-url]
* [![Flask][Flask.com]][Flask-url]
* [![MongoDB][MongoDB.com]][MongoDB-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these simple example steps.

### Prerequisites
 * GitHub Desktop: used to assess repository for cloning, branching, etc.
	* Download at https://desktop.github.com/ 
	* Login and set repository to https://github.com/dinobenj/GlacierProject
	* Clone repository through Git Bash:
	  ```sh
	  $ git clone https://github.com/dinobenj/GlacierProject
	  ```
* R: the language starter files will be in!
 	* Download at:
 	* https://archive.linux.duke.edu/cran/bin/windows/base/ OR
 	* Any other link under USA at https://cran.r-project.org/mirrors.html	 
 * RStudio: used for compiling and running code
 	* Download at https://www.rstudio.com/products/rstudio/download/#download 
* 7-Zip: used to unzip the starter files you'll be provided 
 	* Download at https://www.7-zip.org/download.html
 	* Files can be found in [the Discord:](https://discord.com/channels/1020185003864358942/1020185004313161760/1020446411709493359) 
 * Node
 	* Check if Node is installed & version in command prompt
	  ```sh
	  node -v
	  ```
 	* Follow instructions on this website to update: https://phoenixnap.com/kb/update-node-js-version OR
 	* Install Node at https://nodejs.org/en/download/ if Node is not installed


### Installation
1. Ask project lead to add a new contributor to the repository
2. Install and unzip .7z starter files
	* Store anywhere that is easy and convenient to access (i.e. desktop)
3. Open RStudio and access unzipped files
4. Set working directory to the folder storing all program files
	* Session --> Set Working Directory --> Choose Directory --> Set as Working Directory
5. Change paths in test_with_all_glaciers to path FROM your working directory
6. Run test_with_all_glaciers first to get data together
7. Run (Ctrl + A, Ctrl + Enter)
	* Install additional libraries as needed upon request by RStudio
8. Update line 32 to gmap_data <- sub_data[, c(1, 7, 8, 3)] if not already done
9. Run app.R
	* Do NOT change paths in this file.



<!-- Known Issues Examples -->
### Known Issues
RStudio Library Package Problems:

Multiple times, while downloading a R library, I ran into an error where RStudio would be unable to find the right place to download it to. In order to remedy this, first make sure you're in the correct directory by opening and right clicking on app.R. Select "set working directory". If this doesn't work, follow the path C:\Users\User\Documents\R\win-library and deleted the 4.0/00LOCK (or whatever version you see) file.

<!-- USAGE EXAMPLES -->
<!-- ## Usage


<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- ROADMAP -->
## Roadmap

End of September:
- Agree on a frontend design
- Agree on and transfer all data to server
- Create a better onboarding guide

End of October:
- Create scripts that predict glacier mass based on scientific models
- Display satellite data from OpenGeo API
- Improve API
- Bug fixes

End of November:
- Continue to refine October goals and begin implementation of December goals

End of December
- Implement and display glacier mass predictions on app
- UI update
- Display satellite images with highlights on app for each glacier
- Deploy* (BIIIIIIG astrix) 


See the [open issues](https://github.com/dinobenj/GlacierProject/issues) for a full list of known issues.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE.txt](https://github.com/dinobenj/GlacierProject/blob/main/LICENSE) for more information.

<!-- ACKNOWLEDGMENTS
## Acknowledgments

* []()
* []()
* []()  -->



<!-- CONTACT -->
## Contact

Your Name - [@Cool_Kid420](https://twitter.com/username) - dino.benj11@gmail.com

Project Link: [https://github.com/dinobenj/GlacierProject](https://github.com/dinobenj/GlacierProject)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/dinobenj/GlacierProject.svg?style=for-the-badge
[contributors-url]: https://github.com/dinobenj/GlacierProject/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dinobenj/GlacierProject.svg?style=for-the-badge
[forks-url]: https://github.com/dinobenj/GlacierProject/network/members
[stars-shield]: https://img.shields.io/github/stars/dinobenj/GlacierProject.svg?style=for-the-badge
[stars-url]: https://github.com/dinobenj/GlacierProject/stargazers
[issues-shield]: https://img.shields.io/github/issues/dinobenj/GlacierProject.svg?style=for-the-badge
[issues-url]: https://github.com/dinobenj/GlacierProject/issues
[license-shield]: https://img.shields.io/github/license/dinobenj/GlacierProject.svg?style=for-the-badge
[license-url]: https://github.com/dinobenj/GlacierProject/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Glacier Project Logo]: https://github.com/dinobenj/GlacierProject/blob/main/glacierProjectLogo.png


[Typescript.com]: https://img.shields.io/badge/Typescript-blue?style=for-the-badge&logo=typescript&logoColor=white
[Typescript-url]: https://www.typescriptlang.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[RShiny.com]: https://img.shields.io/badge/RShiny-F2F8FC?style=for-the-badge&labelColor=F2F8FC&logo=RStudio&logoColor=blue
[RShiny-url]: https://shiny.rstudio.com/
[MongoDB.com]: https://img.shields.io/badge/MongoDB-00684A?style=for-the-badge&logo=mongodb&logoColor=00ED64
[MongoDB-url]: https://www.mongodb.com/
[Flask.com]: https://img.shields.io/badge/Flask-white?style=for-the-badge&logo=flask&logoColor=262626
[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/

Footer
© 2022 GitHub, Inc.
Footer navigation
[Terms](https://docs.github.com/en/github/site-policy/github-terms-of-service)
[Privacy](https://docs.github.com/en/github/site-policy/github-privacy-statement)
[Security](https://github.com/security)
[Status](https://www.githubstatus.com/)
[Docs](https://docs.github.com/)
[Contact GitHub](https://support.github.com/?tags=dotcom-footer)
[Pricing](https://github.com/pricing)
[API](https://docs.github.com/)
[Training](https://services.github.com/)
[Blog](https://github.blog/)
[About](https://github.com/about)

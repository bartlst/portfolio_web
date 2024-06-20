import '../styles/MainMenu.css'
function MainMenu(){
    return(<>
    <nav className="mainNavigation">
        <img className="mainNavigation-logo" src="https://placehold.jp/150x150.png"></img>
        <ul className="mainNavigation-menu">
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Projects</a></li>
        </ul>
    </nav></>)
}

export default MainMenu
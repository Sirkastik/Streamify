<template>
    <div class="dropdown">
      <button class="dropbtn">
        <div class="category">All Music</div>
        <div class="down"><i class="fas fa-sort-down"></i></div> 
      </button>

      <div class="dropdown-content">
        <a href="#">All Music</a>
        <a href="#">Favourites</a>
        <a href="#">Added Music</a>
      </div>
    </div>
</template>

<script>
export default {
    name: "DropBtn"
}
</script>

<style scoped>
/* Dropdown Button */
.dropbtn {
  background: none;
  border: 2px solid white;
  color: white;
  padding: 5px 20px;
  font-size: 16px;
  border-radius: 8px;

  display: flex;
  gap: 5px; 
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

.down {
  display: grid;
  justify-content: space-around;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  left: -37%;
  display: none;
  position: absolute;
  background-color: var(--main);
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
  border-radius:10px;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: white;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  border-radius: inherit;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {
  background-color: var(--darker);
  color: var(--accent);
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
  display: block;
}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {
  border: 2px solid#fe5046;
  color: #fe5046;
}
</style>
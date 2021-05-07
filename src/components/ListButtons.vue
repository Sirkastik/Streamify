<template>
  <div class="listNav">
    <div class="funcbutton">
      <button id="sort">
        <i class="fas fa-sort-alpha-up"></i>
      </button>
      <button>
        <i class="fas fa-plus"></i>
      </button>
      <button>
        <i class="fas fa-search"></i>
      </button>
    </div>

    <div class="dropdown">
      <button class="dropbtn">
        <div id="category">All Music</div> 
        <div class="down"><i class="fas fa-sort-down"></i></div>
      </button>

      <div class="dropdown-content">
        <a href="#">All Music</a>
        <a href="#">Favourites</a>
        <a href="#">Added Music</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ListButtons",
};
</script>

<style scoped>
.listNav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}


.funcbutton button {
  font-size: 0.9rem;
  border-radius: 5px;
  color: white;
  outline: none;
  border: none;
  padding: 5px 10px;
  margin: 0 8px;
  background: var(--main);
  box-shadow: 1px 1px 3px 1px hsla(0, 0%, 0%, 0.473);
}

button:hover {
    color: var(--accent);
    background: var(--darker);
}

.down {
  display: grid;
  justify-content: space-around;
}


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
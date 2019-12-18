
<style>
.wiki-container {
    text-align:left;
}
</style>
<div class="wiki-container">    
   <ol class="nav" style="list-style-type:none">   
     {% for name, path in theme.wiki %}
     <li class="nav-item nav-level-1"><a nav-link href="{{path}}">{{ name }}</a></li>  
     {% endfor %}  
   </ul>   
 </div> 


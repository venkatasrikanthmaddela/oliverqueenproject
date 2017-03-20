/**
 * Created by srikanthmv on 19/3/17.
 */

(function(){

    'use strict';

    angular.module('projectsListPageApp',[])
        .controller('ProjectsListPageController', ProjectsListPageController)
        .service('ProjectsListPageService', ProjectsListPageService);

    ProjectsListPageController.$inject=['ProjectsListPageService'];
    function ProjectsListPageController(ProjectsListPageService){
        var projectsObjects = this;

        var activeProjectsPromise = ProjectsListPageService.getAllActiveProjects();

        activeProjectsPromise.then(function(response){
            projectsObjects.allProjects = response.data;
            console.log(response.data);
        }).catch(function(error){
            console.log("something went wrong..")
        });
    }

    //angular.module('MenuCategoriesApp', [])
    //    .controller('MenuCategoriesController', MenuCategoriesController)
    //    .service('MenuCategoriesService', MenuCategoriesService);
    //
    //MenuCategoriesController.$inject = ['MenuCategoriesService'];
    //function MenuCategoriesController(MenuCategoriesService){
    //    var menu = this;
    //
    //    var promise = MenuCategoriesService.getMenuCategories();
    //
    //    promise.then(function(response){
    //            menu.categories = response.data;
    //        })
    //        .catch(function(error){
    //            alert("something went wrong");
    //        });
    //
    //    menu.logMenuItems = function(shortName){
    //        var promise = MenuCategoriesService.getForMenuCategory(shortName);
    //        promise.then(function(response){
    //                console.log(response.data);
    //            })
    //            .catch(function(error){
    //                console.log("something ent wrong again");
    //            })
    //    };
    //}
    //

    ProjectsListPageService.inject=['$http'];
    function ProjectsListPageService($http){
        var service = this;

        service.getAllActiveProjects = function(){
            var response = $http({
                method:"GET",
                url:("http://192.168.1.13:8090/api/projects/get-projects")
            });
            return response
        }
    }
    //MenuCategoriesService.$inject = ['$http'];
    //function MenuCategoriesService($http){
    //    var service = this;
    //
    //    service.getMenuCategories = function(){
    //        var response = $http({
    //            method:"GET",
    //            url:("http://davids-restaurant.herokuapp.com/categories.json")
    //        });
    //
    //        return response;
    //    };
    //
    //    service.getForMenuCategory = function(shortName){
    //        var response = $http({
    //            method:"GET",
    //            url:("http://davids-restaurant.herokuapp.com/categories.json"),
    //            params: {
    //                category:shortName
    //            }
    //        });
    //
    //        return response;
    //    }
    //}
})();
package C20190320;

import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.*;
import java.util.stream.Collectors;

public class DependencyResolver {
    private static class CourseData {

        private Set<String> resolveOrder = new LinkedHashSet<>();
        private Map<String,Course> courses = new HashMap<>();
        private Set<String> pendingResolve = new HashSet<>();

        private void addCourse(String courseName, String... dependencies){
            Course course = getCourse(courseName);
            Arrays.stream(dependencies)
                    .map(this::getCourse)
                    .forEach(course::addDependency);
        }

        private Course getCourse(String name){
            return courses.computeIfAbsent(name, nm -> new Course(nm, this));
        }

        private List<String> resolve() throws Exception {

            List<Course> courseList = courses.values().stream()
                    .filter(crs -> !crs.isDependency()).collect(Collectors.toList());

            courseList.forEach(Course::resolve);

            if(!courses.isEmpty()){
                throw new Exception("Failed to resolve dependency");
            }

            return new ArrayList<>(resolveOrder);
        }


    }

    private static class Course{
        private Map<String, Course> dependencies = new HashMap<>();
        private String name;

        private boolean isDependency() {
            return dependency;
        }

        private boolean dependency = false;
        private CourseData courseData;
        private Course(String name, CourseData courseData){
            this.name = name;
            this.courseData = courseData;
        }

        private void addDependency(Course course){
            dependencies.put(course.name, course);
            course.dependency = true;
        }

        private boolean resolve(){

            //For detecting cyclic dependencies//
            if(courseData.pendingResolve.contains(name)) {
                return false;
            }
            courseData.pendingResolve.add(name);
            /////////////////////////////////////

            boolean resolved = dependencies.values().stream().allMatch(Course::resolve);

            if(resolved){
                courseData.pendingResolve.remove(name);
                courseData.resolveOrder.add(name);
                courseData.courses.remove(name);
            }
            return resolved;
        }

    }

    @Test
    public void testDependency1() throws Exception {
        CourseData courseData = new CourseData();
        courseData.addCourse("01");
        courseData.addCourse("02", "01");
        courseData.addCourse("03", "02", "01");

        Assert.assertEquals(courseData.resolve(), Arrays.asList("01", "02", "03"));
    }

    @Test
    public void testDependency2() throws Exception {
        CourseData courseData = new CourseData();
        courseData.addCourse("03", "01", "02");
        courseData.addCourse("05", "06", "07");
        courseData.addCourse("04",  "07", "03");

        Assert.assertEquals(courseData.resolve(), Arrays.asList("01", "02", "03", "07", "04", "06", "05"));
    }


    @Test(expectedExceptions = Exception.class)
    public void testCyclicDependency1() throws Exception {
        CourseData courseData = new CourseData();
        courseData.addCourse("03", "01", "02");
        courseData.addCourse("05", "06", "07");
        courseData.addCourse("04",  "07", "03");
        courseData.addCourse("02",  "04");

        courseData.resolve();
    }

    @Test(expectedExceptions = Exception.class)
    public void testCyclicDependency2() throws Exception {
        CourseData courseData = new CourseData();
        courseData.addCourse("03", "01", "02");
        courseData.addCourse("05", "06", "07");
        courseData.addCourse("04",  "07", "03");
        courseData.addCourse("02",  "03");
        courseData.resolve();
    }
}

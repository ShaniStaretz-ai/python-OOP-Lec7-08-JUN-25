# python-OOP-Lec7-08-JUN-25
Recursion, inheritance
* fibonaci function
* inheritance:
  * shape example
  * required import:
      ```
      from abc import ABC,abstractmethod:
        #abstract class
      Class Shape(ABC):
      ```
  * ABC to define clas as abstract
  * in python can create instance of abstract class
  * abstractmethod= can't give implementation in the parent class, only in the child clss.
     ```
     @abstractmethod
     def calc_area(self):
        pass
     ```
    * if the parent can do the action, implement it, otherwise implement it in the chile
  * define child:
    ```
    class Triangle(Shape):
    ```
  * the child **must** implement all abstract methods that the parent didn't
    * if it doesn't, it defined as abstract too.
    * example:
      ```
      @oveeride
      def calc_area(self):
        pass
      ```
    * if there are abstractmethod, it must be abstract class
    * if the class is abstract, its functions don't have to be abstractmethod
    * in inheritance, the clas contain the parent too.
    * in the init of the child, can call the init of the parent:
    ```
    super().__init__('Triangle')
    ``` 

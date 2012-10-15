#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;



double calcReynolds(double rho, double V, double D, double mu){
        double R;
        
        R = (rho*V*D) / mu;
        
        return R;
        }

double calcFrictionFactor(double R, double D, double epsilon)


{
    double f1,f2,rho,V,mu;
      f2 = 0.3164 *pow(R,-0.25);
      f1 = pow((2*log10(((epsilon/D)/3.7)+ (2.51/(R*sqrt(f2))))),-2);
    
    while ( abs(f1 - f2) > 0.000001){
        f2 = f1;
         f1 = pow((2*log10(((epsilon/D)/3.7)+ (2.51/(R*sqrt(f2))))),-2);
        }
        
 return f1;
    
    
    
    }
    
    

double calcPressureLoss(double V, double L, double D, double rho, double mu, double epsilon){
   
   double f1, delta, R;
   
   delta = f1*(L/D)*rho*(pow(V,2)/2);
   
    }

 /*bool doTest(double V, double L, double D, double rho, double mu, double epsilon, double delta_expected){

    double delta_calculated;

    cout << setiosflags(ios::fixed) << setprecision(6);
    cout << "Test Case:\n";
    cout << "V = " << V << endl;
    cout << "L = " << L << endl;
    cout << "D = " << D << endl;
    cout << "rho = " << rho << endl;
    cout << "mu = " << mu << endl;
    cout << "epsilon = " << epsilon << endl;
    cout << "Delta (expected) = " << delta_expected << endl;

    delta_calculated = calcPressureLoss(V, L, D, rho, mu, epsilon);
    cout << "Delta (calculated) = " << delta_calculated << endl;

    if (fabs(delta_calculated-delta_expected) > 0.0001) {
        cout << "TEST FAILED!!!" << endl << endl;
        return false;
    }

    cout << "Test passed" << endl << endl;

    return true;
}
*/
int main(int argc, char *argv[])
{
    

   /*        
    double  R =1, D =1, epsilon =1 ;
   
   
   //statements
  
   
   while (R != 0 && D !=0 && epsilon != 0) {
    
    cout <<endl << "please enter a value for R (all zeros to move to part 2): ";
    cin >> R;
    cout << endl << "please enter a value for D in m (all zeros to move to part 2): ";
    cin >> D;
    cout << endl << "please enter a value for epsilon ( the roughness) in mm (all zeros to move to part 2): " ;
    cin >> epsilon;
    cout << endl;
    
    if (R < 3500 || D <= 0 || D > 1 || epsilon < 0 || epsilon > 1000.0 * 0.05 * D) {
            cout << "** Invalid values ignored **" << endl;
            continue;
        }
    
  
    epsilon = epsilon / 1000;
    cout << calcFrictionFactor(R,D,epsilon);
    
   
    }
    
    double rho, V, mu;
    
    cout << "Reynolds"<<endl;
    cout << "please enter a value for rho"<<endl;
    cin >> rho;
    cout << "Please enter a value for V: " << endl;
    cin>> V;
    cout << "please enter a value for D: "<< endl;
    cin>> D;
    cout << "please enter a value for mu: " << endl;
    cin >> mu;
    
    cout << calcReynolds(rho,V,D,mu);
    */
    
    double R, D, epsilon, rho, V, mu, L, delta_expected;
    
    cout << "please enter a value for epsilon ( the roughness) in mm"<<endl;
    cin >> epsilon;
    cout << "please enter a value for rho (the density of the fluid) in Kg/m^3"<<endl;
    cin >> rho;
    cout << "Please enter a value for V (the velocity of the fluid) in m/s: " << endl;
    cin>> V;
    cout << "please enter a value for D ( the diameter of the pipe) in m: "<< endl;
    cin>> D;
    cout << "please enter a value for mu (the viscosity of the liquid) in N*s/m^2 : " << endl;
    cin >> mu;
    
   cout << calcPressureLoss(V,L,D,rho,mu,epsilon);
    
  // doTest(V, L, D, rho, mu, epsilon, delta_expected);

    
    system("PAUSE");
    return EXIT_SUCCESS;
}

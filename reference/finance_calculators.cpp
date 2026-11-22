// FinWise C++ reference calculator formulas (C++17)
// Compile: g++ -std=c++17 finance_calculators.cpp -o finance
// Run: ./finance
#include <cmath>
#include <iomanip>
#include <iostream>
using namespace std;
double emi(double p,double annualRate,double years){
    double n=years*12, r=annualRate/1200.0;
    if(n<=0) return 0;
    if(r==0) return p/n;
    return p*r*pow(1+r,n)/(pow(1+r,n)-1);
}
double sip(double monthly,double annualReturn,double years){
    double n=years*12, r=annualReturn/1200.0;
    if(r==0) return monthly*n;
    return monthly*(pow(1+r,n)-1)/r*(1+r);
}
double gstTotal(double amount,double ratePercent,bool inclusive){
    double rate=ratePercent/100.0;
    return inclusive?amount:amount*(1+rate);
}
double fd(double p,double annualRate,double years,int frequency=4){
    return p*pow(1+annualRate/(100.0*frequency),frequency*years);
}
double rd(double monthly,double annualRate,double years){
    int n=static_cast<int>(years*12);
    double r=pow(1+annualRate/100.0,1.0/12.0)-1;
    if(r==0) return monthly*n;
    return monthly*(pow(1+r,n)-1)/r*(1+r);
}
int main(){
    cout<<fixed<<setprecision(2);
    cout<<"FinWise C++ reference calculator\n1 EMI  2 SIP  3 GST total  4 FD  5 RD\nChoice: ";
    int c; cin>>c;
    if(c==1){double p,r,y;cout<<"Loan amount, annual rate %, years: ";cin>>p>>r>>y;double m=emi(p,r,y);cout<<"Monthly EMI: Rs "<<m<<"\nTotal repayment: Rs "<<m*y*12<<"\n";}
    else if(c==2){double p,r,y;cout<<"Monthly SIP, expected annual return %, years: ";cin>>p>>r>>y;cout<<"Future value estimate: Rs "<<sip(p,r,y)<<"\n";}
    else if(c==3){double a,r;int inclusive;cout<<"Amount, GST rate %, already inclusive (1=yes, 0=no): ";cin>>a>>r>>inclusive;double total=gstTotal(a,r,inclusive);double base=inclusive?a/(1+r/100):a;cout<<"Base: Rs "<<base<<"\nGST: Rs "<<total-base<<"\nTotal: Rs "<<total<<"\n";}
    else if(c==4){double p,r,y;cout<<"Principal, annual rate %, years: ";cin>>p>>r>>y;cout<<"FD maturity estimate: Rs "<<fd(p,r,y)<<"\n";}
    else if(c==5){double p,r,y;cout<<"Monthly deposit, annual rate %, years: ";cin>>p>>r>>y;cout<<"RD maturity estimate: Rs "<<rd(p,r,y)<<"\n";}
    else cout<<"Invalid choice\n";
}
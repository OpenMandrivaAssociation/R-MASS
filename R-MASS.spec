%global packname  MASS
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          7.3.33
Release:          1
Summary:          Support Functions and Datasets for Venables and Ripley's MASS
Group:            Sciences/Mathematics
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_7.3-33.tar.gz

Requires:         R-grDevices R-graphics R-stats R-utils 

Requires:         R-lattice R-nlme R-nnet R-survival 
BuildRequires:    R-devel Rmath-devel R-grDevices R-graphics R-stats R-utils

BuildRequires:   R-lattice R-nlme R-nnet R-survival 
%description
Functions and datasets to support Venables and Ripley, 'Modern Applied
Statistics with S' (4th edition, 2002).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%{rlibdir}/%{packname}

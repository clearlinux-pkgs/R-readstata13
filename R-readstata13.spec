#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-readstata13
Version  : 0.10.0
Release  : 30
URL      : https://cran.r-project.org/src/contrib/readstata13_0.10.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/readstata13_0.10.0.tar.gz
Summary  : Import 'Stata' Data Files
Group    : Development/Tools
License  : GPL-2.0
Requires: R-readstata13-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R

%description
# readstata13
[![CRAN status](http://www.r-pkg.org/badges/version/readstata13)](https://cran.r-project.org/package=readstata13)
[![Build status](https://github.com/sjewo/readstata13/workflows/R-CMD-check/badge.svg)](https://github.com/sjewo/readstata13/actions?workflow=R-CMD-check)
[![CRAN Downloads](http://cranlogs.r-pkg.org/badges/readstata13)](https://cran.r-project.org/package=readstata13)

%package lib
Summary: lib components for the R-readstata13 package.
Group: Libraries

%description lib
lib components for the R-readstata13 package.


%prep
%setup -q -c -n readstata13
cd %{_builddir}/readstata13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621956951

%install
export SOURCE_DATE_EPOCH=1621956951
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library readstata13
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library readstata13
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library readstata13
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc readstata13 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/readstata13/DESCRIPTION
/usr/lib64/R/library/readstata13/INDEX
/usr/lib64/R/library/readstata13/LICENSE
/usr/lib64/R/library/readstata13/Meta/Rd.rds
/usr/lib64/R/library/readstata13/Meta/features.rds
/usr/lib64/R/library/readstata13/Meta/hsearch.rds
/usr/lib64/R/library/readstata13/Meta/links.rds
/usr/lib64/R/library/readstata13/Meta/nsInfo.rds
/usr/lib64/R/library/readstata13/Meta/package.rds
/usr/lib64/R/library/readstata13/NAMESPACE
/usr/lib64/R/library/readstata13/NEWS
/usr/lib64/R/library/readstata13/R/readstata13
/usr/lib64/R/library/readstata13/R/readstata13.rdb
/usr/lib64/R/library/readstata13/R/readstata13.rdx
/usr/lib64/R/library/readstata13/extdata/datetime.do
/usr/lib64/R/library/readstata13/extdata/datetime.dta
/usr/lib64/R/library/readstata13/extdata/encode.do
/usr/lib64/R/library/readstata13/extdata/encode.dta
/usr/lib64/R/library/readstata13/extdata/encodecp.dta
/usr/lib64/R/library/readstata13/extdata/gen_fac.do
/usr/lib64/R/library/readstata13/extdata/gen_fac.dta
/usr/lib64/R/library/readstata13/extdata/missings.do
/usr/lib64/R/library/readstata13/extdata/missings.dta
/usr/lib64/R/library/readstata13/extdata/missings_lsf.dta
/usr/lib64/R/library/readstata13/extdata/missings_msf.dta
/usr/lib64/R/library/readstata13/extdata/nonint.do
/usr/lib64/R/library/readstata13/extdata/nonint.dta
/usr/lib64/R/library/readstata13/extdata/sp500.stbcal
/usr/lib64/R/library/readstata13/extdata/statacar.do
/usr/lib64/R/library/readstata13/extdata/statacar.dta
/usr/lib64/R/library/readstata13/extdata/underscore.do
/usr/lib64/R/library/readstata13/extdata/underscore.dta
/usr/lib64/R/library/readstata13/help/AnIndex
/usr/lib64/R/library/readstata13/help/aliases.rds
/usr/lib64/R/library/readstata13/help/paths.rds
/usr/lib64/R/library/readstata13/help/readstata13.rdb
/usr/lib64/R/library/readstata13/help/readstata13.rdx
/usr/lib64/R/library/readstata13/html/00Index.html
/usr/lib64/R/library/readstata13/html/R.css
/usr/lib64/R/library/readstata13/include/read_data.h
/usr/lib64/R/library/readstata13/include/read_dta.h
/usr/lib64/R/library/readstata13/include/read_pre13_dta.h
/usr/lib64/R/library/readstata13/include/readstata.h
/usr/lib64/R/library/readstata13/include/statadefines.h
/usr/lib64/R/library/readstata13/include/swap_endian.h
/usr/lib64/R/library/readstata13/tests/testthat.R
/usr/lib64/R/library/readstata13/tests/testthat/test_read.R
/usr/lib64/R/library/readstata13/tests/testthat/test_save.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/readstata13/libs/readstata13.so
/usr/lib64/R/library/readstata13/libs/readstata13.so.avx2
/usr/lib64/R/library/readstata13/libs/readstata13.so.avx512

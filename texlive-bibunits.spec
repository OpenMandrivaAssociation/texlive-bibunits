%global tl_name bibunits
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Multiple bibliographies in one document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibunits
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibunits.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibunits.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibunits.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provide a mechanism to generate separate bibliographies for
different units (chapters, sections or bibunit-environments) of a text.
The package separates the citations of each unit of text into a separate
file to be processed by BibTeX. The global bibliography section produced
by LaTeX may also appear in the document and citations can be placed in
both the local unit and the global bibliographies at the same time. The
package is compatible with koma-script and with the babel French option
frenchb.


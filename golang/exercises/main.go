// examples of golang features

package main

import (
	"fmt"
	"go/ast"
	"go/parser"
	"log"
	"math/bits"
	"os"
	"reflect"
	"time"
	"unsafe"

	"golang.org/x/tools/go/loader"
	"golang.org/x/tools/go/types/typeutil"
)

func main() {

	fmt.Println("Hello, World!")

	var aaa, bbb int = 8, 9
	fmt.Printf("Type: %T Value: %v\n", aaa, bbb)
	var t = 123      //Type Inferred will be int
	var u = "circle" //Type Inferred will be string
	var v = 5.6      //Type Inferred will be float64
	var w = true     //Type Inferred will be bool
	var x = 'a'      //Type Inferred will be rune
	var y = 3 + 5i   //Type Inferred will be complex128

	fmt.Printf("Type: %T Value: %v\n", t, t)
	fmt.Printf("Type: %T Value: %v\n", u, u)
	fmt.Printf("Type: %T Value: %v\n", v, v)
	fmt.Printf("Type: %T Value: %v\n", w, w)
	fmt.Printf("Type: %T Value: %v\n", x, x)
	fmt.Printf("Type: %T Value: %v\n", y, y)

	if len(os.Args) != 3 {
		log.Fatal("Usage: doc <package> <object>")
	}
	//!+part1
	pkgpath, name := os.Args[1], os.Args[2]

	// The loader loads a complete Go program from source code.
	conf := loader.Config{ParserMode: parser.ParseComments}
	conf.Import(pkgpath)
	lprog, err := conf.Load()
	if err != nil {
		log.Fatal(err) // load error
	}

	// Find the package and package-level object.
	pkg := lprog.Package(pkgpath).Pkg
	obj := pkg.Scope().Lookup(name)
	if obj == nil {
		log.Fatalf("%s.%s not found", pkg.Path(), name)
	}
	//!-part1
	//!+part2

	// Print the object and its methods (incl. location of definition).
	fmt.Println(obj)
	for _, sel := range typeutil.IntuitiveMethodSet(obj.Type(), nil) {
		fmt.Printf("%s: %s\n", lprog.Fset.Position(sel.Obj().Pos()), sel)
	}

	// Find the path from the root of the AST to the object's position.
	// Walk up to the enclosing ast.Decl for the doc comment.
	_, path, _ := lprog.PathEnclosingInterval(obj.Pos(), obj.Pos())
	for _, n := range path {
		switch n := n.(type) {
		case *ast.GenDecl:
			fmt.Println("\n", n.Doc.Text())
			return
		case *ast.FuncDecl:
			fmt.Println("\n", n.Doc.Text())
			return
		}
	}
	//!-part2

	//This is computed as const uintSize = 32 << (^uint(0) >> 32 & 1) // 32 or 64
	sizeOfIntInBits := bits.UintSize
	fmt.Printf("%d bits\n", sizeOfIntInBits)

	var a int
	fmt.Printf("%d bytes\n", unsafe.Sizeof(a))
	fmt.Printf("a's type is %s\n", reflect.TypeOf(a))

	b := 2
	fmt.Printf("b's typs is %s\n", reflect.TypeOf(b))

	go start()
	fmt.Println("Started")
	time.Sleep(1 * time.Second)
	fmt.Println("Finished")

	ccc := 2
	ddd := &ccc
	fmt.Println(*ddd)

}

func start() {
	fmt.Println("In Goroutine")
}

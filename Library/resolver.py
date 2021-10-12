from ariadne import MutationType, make_executable_schema, QueryType

from Library.models import Book

type_defs = """

type Query{
    all_books: [Book]
    book(input:BookInput):[Book]
}

type Book {
    id: ID
    author: String
    publisher: String
    cover: String
    published_at:String

}
type Mutation{
    add_book(input: BookInput): BookResults
    update_book(input: BookInput): BookResults
    delete_book(input: BookInput): BookResults

}
input BookInput {
    id: ID
    author: String
    publisher: String
    cover: String
}
  type BookResults {
        successful: Boolean
        book: Book
}

"""

query = QueryType()
mutation = MutationType()


@query.field('all_books')
def resolve_books(*_):
    return Book.objects.all()


@query.field('book')
def resolve_books(_, info, input):
    return Book.objects.filter(id=input['id'])


@mutation.field('add_book')
def resolve_add_book(_, info, input):
    book = Book.objects.create(author=input['author'], publisher=input['publisher'], cover=input['cover'], )
    return {'successful': True, 'book': book}


@mutation.field('update_book')
def resolve_update_book(_, info, input):
    book = Book.objects.get(id=input['id'])
    book.author = input['author']
    book.publisher = input['publisher']
    book.cover = input['cover']
    book.save()
    return {'successful': True, 'book': book}


@mutation.field('delete_book')
def resolve_delete_book(_, info, input):
    book = Book.objects.get(id=input['id'])
    book.delete()
    return {'successful': True}


schema = make_executable_schema(type_defs, query, mutation)

class Post < ApplicationRecord
  has_many :comments, dependent: :destroy
  validates :title, presence: true, length: { minimum: 5 }
  validates :body, presence: true

  # Add the 'online' boolean attribute with default value true
  attribute :online, :boolean, default: true
end

